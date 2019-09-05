
#숫자판별함수
def num_chk(numstr):
    num = int(numstr)
    if num==1:
        return 'bc'
    elif num==2:
        return 'abdeg'
    elif num==3:
        return 'abcdg'
    elif num==4:
        return 'bcfg'
    elif num==5:
        return 'acdfg'
    elif num==6:
        return 'acdefg'
    elif num==7:
        return 'abcfg'
    elif num==8:
        return 'abcdefg'
    elif num==9:
        return 'abcdfg'
    elif num==0:
        return 'abcdef'
    else:
        return 'error'

#배열 값 입력 함수
def ary_inpt(ary,code,kan,s):
    if 'a' in code:
        for i in range(1,s+1):
            ary[0][i+kan*(s+2)]='-'
    if 'b' in code:
        for i in range(1,s+1):
            ary[i][s+1+kan*(s+2)]='|'
    if 'c' in code:
        for i in range(s+2,2*s+2):
            ary[i][s+1+kan*(s+2)]='|'
    if 'd' in code:
        for i in range(1,s+1):
            ary[-1][i+kan*(s+2)]='-'
    if 'e' in code:
        for i in range(s+2,2*s+2):
            ary[i][kan*(s+2)]='|'
    if 'f' in code:
        for i in range(1,s+1):
            ary[i][1+kan*(s+2)]='|'
    if 'g' in code:
        for i in range(1,s+1):
            ary[s+1][i+kan*(s+2)]='-'

    return ary

#숫자 표출 함수
def num_outpt(ary):
    for row in ary:
        print(row)

#메인 함수
def LCD(s,n):
    #숫자 칸수
    kan=0
    #숫자자리수
    cn=str(n)
    #배열 선언, 공간확보를 위한
    ntx = [' ' for _ in range(2*s+3)]
    for p in range(2*s+3):
        ntx[p] = [' ' for _ in range((s+2)*len(cn))]
    #구동
    for i in cn:
        ntx=ary_inpt(ntx,num_chk(i),kan,s)
        kan+=1
    num_outpt(ntx)



LCD(3,123)
