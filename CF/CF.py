from math import sqrt

dataset={
'Lisa Rose': {
'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5,'You, Me and Dupree': 2.5, 'The Night Listener': 3.0
},
'Gene Seymour': {
'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5
},
'Michael Phillips': {
'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0
},
'Claudia Puig': {
'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5
},
'Mick LaSalle': {
'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0
},
'Jack Matthews': {
'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5
},
'Toby': {
'Snakes on a Plane':4.5, 'You, Me and Dupree':1.0, 'Superman Returns':4.0
}
}

# ユーザの類似度を計算
def get_similairty(person1, person2):

  ## 両者とも見た映画の集合を取る
  set_person1 = set(dataset[person1].keys())
  set_person2 = set(dataset[person2].keys())
  set_both = set_person1.intersection(set_person2)

  if len(set_both)==0: #共通でみた映画がない場合は類似度を0とする
    return 0

  list_destance = []

  for item in set_both:
    # 同じ映画のレビュー点の差の2乗を計算
    # この数値が大きいほど「気が合わない」=「似ていない」と定義できる 
    distance = pow(dataset[person1][item]-dataset[person2][item], 2) 
    list_destance.append(distance)

  return 1/(1+sqrt(sum(list_destance))) #各映画の気の合わなさの合計の逆比的な指標を返す

def get_recommend(person, top_N):

  totals = {} 
  simSums = {} 

  # 自分以外のユーザのリストを取得してFor文を回す
  # -> 各人との類似度、及び各人からの（まだ本人が見てない）映画の推薦スコアを計算するため
  list_others = list(dataset.keys())
  list_others.remove(person)

  for other in list_others:
    # 本人がまだ見たことが無い映画の集合を取得
    set_other = set(dataset[other])
    set_person = set(dataset[person])
    set_new_movie = set_other.difference(set_person)

    # あるユーザと本人の類似度を計算(simは0~1の数字)
    sim = get_similairty(person, other)

    # (本人がまだ見たことがない)映画のリストでFor分を回す
    for item in set_new_movie:

      # "類似度 x レビュー点数" を推薦度のスコアとして、全ユーザで積算する
      totals.setdefault(item,0)
      totals[item] += dataset[other][item]*sim 

      # またユーザの類似度の積算値をとっておき、これで上記のスコアを除する
      simSums.setdefault(item,0)
      simSums[item] += sim

  rankings = [(total/simSums[item],item) for item,total in totals.items()]
  rankings.sort()
  rankings.reverse()

  return [i[1] for i in rankings][:top_N]

if __name__ == '__main__':
    print(get_recommend('Toby',2))

