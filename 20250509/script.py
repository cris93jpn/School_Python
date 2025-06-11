'''
P-163  List9-1 モジュールとパッケージを切り分ける
'''
import my_func
import my_class
#---関数やクラスを利用している部分　ここから---#

result1 = my_func.plus(10, 3)
result2 = my_func.minus(10, 3)

print('10 + 3 =', result1)
print('10 - 3 =', result2)

account1 = my_class.Account('佐藤', 1, 1000)
account1.show_detail()

#---関数やクラスを利用している部分　ここまで---#
