'''
おみくじ
'''
import random
#おみくじのリスト
lst = ['大吉', '中吉', '小吉', '凶', '大凶']
#3回まで
for i in range (3):
    #質問
    num = int(input('おみくじを引きますか？ YES: 1, NO: 2'))
    #はい場合ランダムを引きます
    if num == 1:
        dice = random.choice(lst)
        #表示
        print(dice)
        continue
    #いいえの場合は終了
    elif num == 2:
        print('おみくじを終了します。')
        break
    #他の番号の場合エラー
    else:
        print('番号が違います。')
