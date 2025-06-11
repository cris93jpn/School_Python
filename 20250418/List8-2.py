'''
P-151 リスト８－２
'''


#クラス定義
class Student:
    #初期化用メソッド
    def __init__(self):
        self.name = ''
        self.math = 0
        self.english = 0
        self.japanese = 0

#メイン
#インスタンス生成
stu1 = Student()
print(type(stu1))
