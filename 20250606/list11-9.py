'''
P-199 ファイルへの書き込み
''' 
f = open('writesample.txt', 'w', encoding='utf-8')
txt = '''abc
def
efg '''
f.write(txt)
f.close()