def main():

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

if __name__ == '__main__':
    main(
