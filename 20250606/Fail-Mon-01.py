'''
Fail-Mon-01
'''

#読み込む
f = open('students3.txt', 'w', encoding='utf-8')
txt = '''
高野, 45, 67, 90
丸山, 64, 98, 79
三村, 48, 87, 92
'''
f.write(txt)
f.close()

#追加書き込み
f = open('students3.txt', 'a', encoding='utf-8')
txt2 = '''
柴田，100，40，65
古川，83，81，74
'''
f.write(txt2)
f.close()

#表示リスト形式
f = open('students3.txt', encoding='utf-8') 
list1 = f.readlines()
print(list1)
f.close()
