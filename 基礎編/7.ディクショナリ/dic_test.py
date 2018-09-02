print('ディクショナリの基本')
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('--------------------------------')

print('valueの取得')

test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

print(test_dict_1['YEAR'])
#print(test_dict_1['YEARS'])

print('---------------------------------')

print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS'))

print('---------------------------------')

print(test_dict_1.get('YEAR','NOT FOUND'))
print(test_dict_1.get('YEARS','NOT FOUND'))

print('要素の追加')
test_dict_1 = {}

print(test_dict_1)

print('=================================')

test_dict_1['YEAR']  = '2010'
test_dict_1['MONTH'] = '1'
test_dict_1['DAY']   = '20'

print(test_dict_1)

print('要素の削除')
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

del test_dict_1['DAY']

print(test_dict_1)

print('keyやvalueだけを取得する')
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

print(test_dict_1.keys())
print(test_dict_1.values())

print('keyとvalueを同時に取得する')
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')

for key, value in test_dict_1.items():
    print(key, value)

print('keyを保持しているの確認')
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}

print(test_dict_1)

print('=================================')
print('YEAR' in test_dict_1)
print('YEARS' in test_dict_1)
