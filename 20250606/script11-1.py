'''
P-203 問題1
'''
f = open('students.txt', 'w', encoding='utf-8')
txt = '''
#名前, 数学, 英語, 国語
丸山, 64, 98, 79
三村, 48, 87, 92
佐藤, 100, 40, 65
古川, 83, 81, 74
'''
f.write(txt)
f.close()