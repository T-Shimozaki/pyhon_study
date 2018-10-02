import os

test_1 = '1234'
test_2 = '5678'

print('test_1 =' + test_1)
print('test_2 =' + test_2)

print(os.path.join(test_1,test_2))
print(os.path.join(test_1,'9999',test_2))
