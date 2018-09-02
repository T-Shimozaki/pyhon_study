print('セットの基本')
test_set1 = {'AAA','BBB','CCC','DDD'}
print(test_set1)
for i in test_set1:
    print(i)


print('セットの追加')
test_set1 = set()
print(test_set1)
test_set1.add('AAA')
test_set1.update({'BBB','CCC','DDD'})
print(test_set1)

print('削除')
test_set_1 = {'python', '-', 'izm', '.', 'com'}

test_set_1.remove('-')
test_set_1.discard('.')

print(test_set_1)

print('frozenset')
test_set2 = frozenset({'CCC','DDD','AAA','BBB'})
print(test_set2)
