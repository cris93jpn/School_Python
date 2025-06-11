'''
P-154 リスト8-8
'''

#クラス定義
class Student:
    def __init__(self, in_name, in_math, in_eng, in_jpn):
        #初期化用メソッド 引数有
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn

#メイン
#インスタンス生成
stu1 = Student('佐藤', 90, 60, 70)
print('生徒名', stu1.name)
print('数字', stu1.math)
print('英語', stu1.english)
print('国語', stu1.japanese)

#データの更新
stu1.japanese = 75
print('更新後の国語', stu1.japanese)