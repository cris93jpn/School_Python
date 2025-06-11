'''
誕生日
'''

from datetime import date, datetime, timedelta
birth = datetime(1993, 5, 13)
today = date.today()
#誕生日
days = date.today()- date(1993, 5, 13)
age = today.year - birth.year
#年齢
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1
#誕生日の表示
dt = birth.strftime('%Y年%m月%d日%A')
print(dt)
#何日誕生日から
print(days)
#歳
print(age, '歳')
