'''
P-182 乱数を作る
randomモジュール
'''
import random
rd = random.random()
print(rd)

#P-182 指定した範囲
dice = random.randint(1,6)
print('サイコロの目は', dice, 'です')

#P-183 リストなど、あらランダムに要素を取り出す
lst = [10, 3.14, 'abc', (5, 10, 15)]
el = random.choice(lst)
print(el)