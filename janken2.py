import random

# じゃんけんの手をリストで定義
hands = ["ぐー", "ちょき", "ぱー"]

# 勝敗を判定するためのルールを辞書で定義
# (自分の手, 相手の手): 結果 (0: 引き分け, 1: 勝ち, -1: 負け)
results = {
    (0, 0): 0, (0, 1): 1, (0, 2): -1,
    (1, 0): -1, (1, 1): 0, (1, 2): 1,
    (2, 0): 1, (2, 1): -1, (2, 2): 0
}
point=0
for i in range (3):
    while True:
        # コンピュータの手をランダムに選択
        en = random.randint(0, 2)

        # ユーザーの手を入力
        try:
            my = int(input("ぐー: 0, ちょき: 1, ぱー: 2 -> "))
            if my not in [0, 1, 2]:
                raise ValueError
        except ValueError:
            print("不正な入力です。正しい数値を入力してください。")
            continue

        # 勝敗判定
        result = results[(my, en)]

        # 結果を表示
        print(f"Aの手: {hands[my]} v.s. Bの手: {hands[en]}")

        if result == 0:
            print("引き分け！再勝負！")
        elif result == 1:
            print("Aの勝ち")
            point+=1
            print("point: ",point)
            break
        else:
            print("Bの勝ち")
            point-=1
            print("point: ",point)
            break
if point>=1:
    print("最終結果:Aの勝ち")
else:
    print("最終結果:Bの勝ち")