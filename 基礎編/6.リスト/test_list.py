test_list_1 = ['python', '-', 'izm', '.', 'com']
print(test_list_1)

for i in test_list_1:
    print(i)

test_list_2 = ['python', 'izm', 'com']
print(test_list_2)
test_list_2.insert(1,'-')
test_list_2.insert(3,'.')
print(test_list_2)
test_list_2.insert(0,'aaa')
print(test_list_2)

test_list_2.append('/sample')
print(test_list_2)

test_list_2.remove('com')
print(test_list_2)

test_list_2.pop(1)
print(test_list_2)

#indexは0からスタート
print(test_list_1.index('com'))
test_list_1.append('aaa')
test_list_1.append('aaa')
test_list_1.append('aaa')
print(test_list_1.count('aaa'))
