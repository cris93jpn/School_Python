'''
P-158 練習問題１
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
        
#メインーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


students = []
#5人分の情報を入力
for i in range (5):
    name = input('生徒名を入力してくださいー＞')
    mth = int(input('数字の点数を入力してくださいー＞'))
    eng = int(input('英語の点数を入力してくださいー＞'))
    jpn = int(input('国語の点数を入力してくださいー＞'))
    stu = Student(name, mth, eng, jpn)
    students.append(stu)

print()

#生徒の表示
for i in range(5):
    students[i].show_detail()
    print()
