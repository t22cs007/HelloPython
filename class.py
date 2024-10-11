import random
class Player:
    '''
    プレイヤークラスのコンストラクタ
    引数:nameプレイヤーの名前
    '''
    def __init__(self,name):
        self._name=name
        self.wincount=0
        
    '''
    じゃんけんの手を出す関数：
    0,1,2をランダムに出力する
    '''
    def show_hand(self):
        return random.randrange(3)
    
    '''
    審判から勝敗を聞く
    '''
    def notify_result(self,result):
        if True == result:
            self._wincount += 1
    
    '''
    自分の勝ちの数を数える
    '''
    def get_wincount(self):
        return self._wincount
    
    '''
    名前を答える（表示する）
    '''
    def get_name(self):
        return self._name
    
class Judge:
    #審判クラスのコンストラクタなしお
    
    '''
    じゃんけんの手と数値の対応（クラス定数として定義）
    グー＝０
    ちょき＝１
    パー＝２
    '''
    def print_hand(self,hand):
        if hand == 0:
            return 'ぐー'
        elif hand == 1:
            return 'ちょき'
        elif hand == 2:
            return 'ぱ-'
    '''
    じゃんけんを一回実行して、勝者を返す
    '''
    def judge_janken(self, player1, player2):
        winner = None
        player1Hand = player1.show_hand()
        player2Hand = player2.show_hand()
        
        print(player1.get_name(), '：', Judge.print_hand(self, player1Hand), 
            ' v.s. ', 
            player2.get_name(), '：', Judge.print_hand(self, player2Hand))
        
        if (player1Hand == 0 and player2Hand == 1) or (player1Hand == 1 and player2Hand == 2) or \
        (player1Hand == 2 and player2Hand == 0):
            winner = player1
        elif (player2Hand == 0 and player1Hand == 1) or (player2Hand == 1 and player1Hand == 2) or \
            (player2Hand == 2 and player1Hand == 0):
            winner = player2
        
        return winner
    '''
    最終的な勝者を判定する
    '''
    def judge_finalwinner(self, player1, player2):
        winner = None
        player1Wincount = player1.get_wincount()
        player2Wincount = player2.get_wincount()
        
        if player1Wincount > player2Wincount:
            winner = player1
        elif player2Wincount > player1Wincount:
            winner = player2
        
        return winner
    '''
    じゃんけんプログラムの本体
    '''
    def start_janken(self, player1, player2):
        print('【じゃんけん開始】')
        
        for x in {1, 2, 3}:
            print('【', x, '回戦目】')
            winner = Judge.judge_janken(self, player1, player2)
            
            if winner is not None:
                print(winner.get_name(), 'の勝ち')
                winner.notify_result(True)
            else:
                print('引き分け')
        
        print('【じゃんけん終了】')
        finalWinner = Judge.judge_finalwinner(self, player1, player2)
        print(player1.get_wincount(), '対', player2.get_wincount(), 'で')
        
        if finalWinner is not None:
            print(finalWinner.get_name(), 'の勝ちです')
        else:
            print('引き分けです')

