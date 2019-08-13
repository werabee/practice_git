
#문제 7-1
print('[문제 7-1]')

import os
f1 = open('c:\\Users\\DongbinShin\\Desktop\\number.txt', 'wt')
for i in range(1, 11):
        f1.write("%d\n" % i)
f1.close()

print('\n')

#문제 7-2
print('[문제 7-2]')

import os
def flist(path):
    f = open('c:\\Users\\DongbinShin\\Desktop\\flist.txt', 'wt')
    flist = os.listdir(path)
    for x in flist:
        f.write('%s\n' % x)
    f.close()
flist(input('경로를 입력하세요 : '))


