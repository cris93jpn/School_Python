'''
P-177 日付や時間の差分の表示
timedeltaクラスをインポート
'''

from datetime import date, datetime, timedelta

#1日前のdatetimeを取得
nd = date.today() - timedelta(days=1)
print(nd)

#3時間後のdateを取得
hd = datetime.now() + timedelta(hours=3)
print(hd)

#2000/3/10から2000/3/3までの差分
td1 = date(2000, 3, 10) - date(2000, 3, 3)
print(td1.days)

#2000/3/3 10:00から2000/3/3 10:30までの秒数
td2 = datetime(2000, 3, 3, 10, 30) - datetime(2000, 3, 3, 10, 00)
print(td2.seconds)
