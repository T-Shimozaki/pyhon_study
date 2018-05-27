import datetime

today = datetime.date.today()
today_detail = datetime.datetime.today()

#普通に表示
print(today)
print(today_detail)

#個別
print(today.year)
print(today.month)
print(today.day)
print(today_detail.year)
print(today_detail.month)
print(today_detail.day)
print(today_detail.hour)
print(today_detail.minute)
print(today_detail.second)
print(today_detail.microsecond)

# 日付のフォーマット
print(today.isoformat())
print(today_detail.strftime("%Y/%m/%d %H:%M:%S"))
