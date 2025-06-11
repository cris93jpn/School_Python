'''
P-163  List9-1 モジュールとパッケージを切り分ける
'''

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