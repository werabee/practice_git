﻿
# 두 날짜(YYYYMMDD)의 차이 일수를 구하는 프로그램을 작성하시오.
# ※ 단, 프로그래밍 언어에서 지원하는 날짜차이를 계산하는 라이브러리는 사용하지 말것
# 예)
# 20070515 sub 20070501 = 14
# 20070501 sub 20070515 = 14
# 20070301 sub 20070515 = 75

#달력
Cal = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

#입력값 체크
def InputCheck(x, y, z):
    if y > 12:
        return 1
    if ((x % 4 or x % 100) and x % 400):
        if y == 2:
            z > Cal['2'] + 1
            return 0
        elif z > Cal['%d' % y] or z<0:
            return 1
    return 0


#년월일을 일수로 치환
def num(A):
    a = str(A)
    a1 = int(a[0:4])
    a2 = int(a[4:6])
    a3 = int(a[6:8])
    A = InputCheck(a1,a2,a3)
    if InputCheck(a1,a2,a3):
        return '날짜입력이 잘못되었습니다'
    sum1 = a1 * 365 + a1 // 4 - a1 // 100 + a1 // 400
    sum2 = sum(list(Cal[str(i)] for i in range(1, a2 + 1)))
    sum3 = a3
    return int(sum1 + sum2 + sum3)

#두 날짜의 차이 반환
def chai(A, B):
    return abs(num(A)-num(B))

chai(20190827,20180827)
#값은 365일 것이다
