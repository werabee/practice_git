
#문제 5-1
print('[문제 5-1]')
def maverage(a,b):
    return (a+b)/2

print("두 값을 입력하시오")
a=int(input())
b=int(input())
c=maverage(a,b)
print("두값의 평균은 ",c)
print('\n')

#문제 5-2
print('[문제 5-2]')
def get_max_min(data_list):
    return (max(data_list),min(data_list))

print("숫자 다섯개를 넣으시오")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
data_list=[a,b,c,d,e]
print('당신이 선택한 숫자',data_list)
f=get_max_min(data_list)
print('최대값은 ',f[0],'최소값은',f[1])
print('\n')

#문제 5-3
print('[문제 5-3]')
import os
def get_txt_list(path):
    b=os.listdir(path)
    c=[]
    for a in b:
        if a.endswith('txt'):
            c.appened(a)
    return c

print('경로를 입력하세요:',end=' ')
path=input()
ab=get_txt_list(path)
print('경로에 존재하는 txt 파일은:',ab)
print('\n')

#문제 5-4
print('[문제 5-4]')
def get_BMI(kg1,cm1):
    bmi = kg1/cm1
    a=[18.5, 25.0, 30.0, 300.0]
    b=['마른체형','표준','비만','고도비만']
    for i in range(0,4):
        if bmi < a[i]:
            print(b[i])
            break
print('\n')

#문제 5-5
print('[문제 5-5]')
def get_BMI(kg1,cm1):
    bmi = kg1/cm1
    a=[18.5, 25.0, 30.0, 300.0]
    b=['마른체형','표준','비만','고도비만']
    for i in range(0,4):
        if bmi < a[i]:
            return (bmi,(b[i]))

#while 100:
print('몸무게를 입력하세요 : ',end=' ')
kg1=int(input())
print('키를 입력하세요 : ',end=' ')
cm1=int(input())
bmi=get_BMI(kg1,cm1)
print('\n당신의 BMI는 : ',bmi[0],'이고.\n당신은 ',bmi[1],'입니다.\n')
print('\n')

#문제 5-6
print('[문제 5-6]')
def get_triangle_area(width, height):
    area = width*height*0.5
    return area

print('삼각형의 길이를 입력하시오 :',end=' ')
a=int(input())
print('삼각형의 높이를 입력하시오 :',end=' ')
b=int(input())
c=get_triangle_area(a,b)
print('삼각형의 넓이는 ',c)
print('\n')

#문제 5-7
print('[문제 5-7]')

def add_start_to_end(start, end):
    a=range(start,end+1)
    b=(a[0]+a[-1])*(a[-1]+1-a[0])/2
    #또는
    #b=0
    #for i in a:
    #    b = b + i
    return b
print("시작값을 넣으시오 :",end=' ')
a=int(input())
print("마지막 값을 넣으시오 :",end=' ')
b=int(input())
c=add_start_to_end(a,b)
print("당신이 선택한 구간의 정수합은: ",c)

print('\n')