'''
P203 問題2
'''

f = open('students.txt', 'a', encoding='utf-8')
stu = []
name = input('生徒名を入力してくださいー＞')
mth = int(input('数字の点数を入力してくださいー＞'))
eng = int(input('英語の点数を入力してくださいー＞'))
jpn = int(input('国語の点数を入力してくださいー＞'))
txt = str(name) + ', ' + str(mth) + ', ' + str(eng) + ', ' + str(jpn)
f.write(txt)
f.close()