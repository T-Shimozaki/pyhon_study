#javaでいうsplit?
#sequence[<開始位置>:<終了位置>:<ステップ幅>]で記載
#開始位置はその要素以降、終了位置はその要素まで、ステップ幅は取得間隔
test_list = ['https', 'www', 'python', 'izm', 'com']
print(test_list[:4])
print(test_list[2:])
print(test_list[::2])
print(test_list[3:5])

print(test_list[-1:])   # 末尾から全ての要素
print(test_list[:-1])   # 末尾まで全ての要素
print(test_list[::-1])  # 末尾から全ての逆順要素

test_list = ['https', 'www', 'python', 'izm', 'com']

test_list[1:3] = ('WWW', 'PYTHON')

print(test_list)
