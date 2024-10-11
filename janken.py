import random
random.seed()

def check(my,en):
    
    if my == en:
        tmp = 1
    if my == 0:
        if en == 1:
            tmp = 0
        if en == 2:
            tmp = 2
    elif my == 1:
        if en == 0:
            tmp = 2
        if en == 2:
            tmp = 0
    elif my == 2:
        if en == 0:
            tmp = 0
        if en == 1:
            tmp = 2
    if tmp == 0:
        return "Aの勝ち"
    elif tmp == 1:
        return "引き分け"
    elif tmp == 2:
        return "Bの勝ち"

en = random.randint(0,2)
if en == 0:
    enstr = "ぐー"
elif en == 1:
    enstr = "ちょき"
elif en == 2:
    enstr = "ぱー"
my = int(input("ぐー: 0, ちょき: 1, ぱー: 2 ->"))
if my == 0:
    mystr = "ぐー"
elif my == 1:
    mystr = "ちょき"
elif my == 2:
    mystr = "ぱー"
check = check(my,en)
# print("あいて:",enstr)
# print("じぶん:",mystr)



print("Aの手: ",mystr," v.s. Bの手: ",enstr," -> ",check)

