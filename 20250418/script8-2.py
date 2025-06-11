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
    
    #合計点の最大値を求めるメソッドを追加
    def get_bigger_score(self, students):
        max_score = 0
        top_stu = None
        for student in students:
            tot = student.get_total_score()
            if tot > max_score:
                max_score = tot
                top_stu = student
        return top_stu 


        
#メイン

students = []
#5人分の情報を入力
for i in range (3):
    name = input('生徒名を入力してくださいー＞')
    mth = int(input('数字の点数を入力してくださいー＞'))
    eng = int(input('英語の点数を入力してくださいー＞'))
    jpn = int(input('国語の点数を入力してくださいー＞'))
    stu = Student(name, mth, eng, jpn)
    students.append(stu)

print()

#生徒の表示
for i in range(3):
    students[i].show_detail()
    tot_sc = students[i].get_total_score()
    print('合計点：', tot_sc)
    avr = students[i].get_average_score(tot_sc)
    print('平均点：', avr)
    print()

#最大合計を持つ生徒を表示
top = students[0].get_bigger_score(students)
print('一番高い点数の学生は：')
top.show_detail()