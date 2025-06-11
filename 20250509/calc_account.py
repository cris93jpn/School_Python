'''
P-163  List9-1 モジュールとパッケージを切り分ける
'''

#---関数を定義している部分　ここから---#
def plus(x=0, y=0):
    return x + y
def minus(x=0, y=0):
    return x -y
#---関数を定義している部分　ここまで---#

#---クラスを定義している部分　ここから---#
class Account:
    def __init__(self, name, no, balance):
        self._name = name
        self._no = no
        self._balance = balance

    def show_detail(self):
        print('口座名義', self._name)
        print('口座番号', self._no)
        print('残高', self._balance)

#---クラスを定義している部分　ここまで---#

#---関数やクラスを利用している部分　ここから---#

result1 = plus(10, 3)
result2 = minus(10, 3)

print('10 + 3 =', result1)
print('10 - 3 =', result2)

account1 = Account('佐藤', 1, 1000)
account1.show_detail()

#---関数やクラスを利用している部分　ここまで---#
