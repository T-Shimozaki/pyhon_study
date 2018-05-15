print("test_ism")
print("test_ism_2")

test_2 = 'aaa'
test_2 = test_2 + "_"
test_2 = test_2 + "bbb"
print(test_2)

#文字列の変換
test_int = 100
print(str(test_int) + "円")

#文字列の置換
test_str = "aaa_bbb"
print(test_str.replace('bbb','ccc'))

#文字列の分割
test_str2 = 'aaa_ccc'
print(test_str2.split('_'))

#桁揃え
str3 = '12345'
print(str3.rjust(10,'?'))
print(str3.ljust(10,'!'))
print(str3.zfill(7))

#検索
str_find = '12345ZZZ'
print('z' in str_find)
print('Z' in str_find)
print('A' in str_find)

#大文字小文字変換
str_a = 'strAaBb'
print(str_a)
print(str_a.upper())
print(str_a.lower())
