

#문제4-1
print('[문제 4-1]')
print('*'*5, end='')
print('\n')

#문제4-2
print('[문제 4-2]')
for i in range(0,4):
    print('*'*5)
print('\n')

    
#문제4-3
print('[문제 4-3]')
for i in range(1,6):
	print('*'*i)
print('\n')

	
#문제4-4
print('[문제 4-4]')
for i in range(0,5):
    print('*'*(5-i))
print('\n')

#문제4-5
print('[문제 4-5]')
for i in range(1,6):
    print(' '*(5-i)+'*'*(i))
print('\n')

#문제4-6
print('[문제 4-6]')
for i in range(0,5):
    print(' '*(i)+'*'*(5-i))
print('\n')

#문제4-7
print('[문제 4-7]')
for i in range(1,6):
    print(' '*(5-i)+'*'*(2*i-1)+' '*(5-i))
print('\n')

#문제4-8
print('[문제 4-8]')
for i in range(1,6):
	print(' '*(i-1)+ '*'*(11-2*i)+' '*(i-1))
print('\n')

#문제4-9
print('[문제 4-9]')
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
for floor in apart:
    for house in floor: 
        if house in arrears :
            continue
        else :
            print('delivery success :',house)
print('\n')
