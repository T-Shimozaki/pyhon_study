import datetime

def get_today():

 today = datetime.date.today()
 value = (today.year,today.month,today.day)

return value


test_tup = get_today()

print(test_tup)
print(test_tup[0])
print(test_tup[1])
print(test_tup[2])
