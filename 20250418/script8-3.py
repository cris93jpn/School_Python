'''
P-159 
'''

#クラス定義
class Student:
    def __init__(self, in_name, in_math, in_eng, in_jpn):
        #初期化用メソッド 
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn

    #自分の情報を表示するメソッド
    def show_detail(self):
        print('生徒名：', self.name)
        print('数字：', self.math)
        print('英語：', self.english)
        print('国語：', self.japanese)

    #一人分の合計するメソッドの定義
    def get_total_score(self):
        tot = self.math + self.english + self.japanese
        return tot
    
    #一人分の平均を求めるメソッドの定義
    def get_average_score(self, tot):
        av = tot / 3
        return av
        
#メイン

students = [Student('佐藤', 100, 40, 65), Student('丸山', 64, 98, 79), Student('三村', 48, 87, 92), Student('古川', 83, 81, 74)]

name1 = input('生徒名を入力してくださいー＞')
flg = True

#リストの参照先の名前を検索

for stu in students:
    if name1 == stu.name:
        stu.show_detail()
        flg = False
        break

#検索してなかった場合
if flg:
    print('存在しません')
