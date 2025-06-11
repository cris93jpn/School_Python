'''
P-179 曜日の取得
文字列から日時への変換
日時から文字列への変換
'''

from datetime import datetime
#文字列から日時
s = '2000年3月3日'
dt = datetime.strptime(s, '%Y年%m月%d日')
print(dt)

#日時から文字列
dt = datetime(2000, 3, 3, 10, 30)
st = dt.strftime('%Y年%m月%d日%p%I:%M')
print(st)

