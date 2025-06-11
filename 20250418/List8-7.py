'''
P-153 リスト8-7
'''

#クラス定義
class Student:
    def __init__(self, in_name = '', in_math = 0, in_eng = 0, in_jpn =0):
        #初期化用メソッド
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn

#メイン
#インスタンス生成
stu1 = Student('佐藤', 90, 60, 70)
print(type(stu1))