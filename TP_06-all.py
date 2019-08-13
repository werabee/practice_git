
#문제 6-1
print('[문제 6-1]')

class Point:
    def __init__(self,xx,yy):
        self.x = xx
        self.y = yy
        print("x:%d, y:%d"%(xx,yy))
    def setx(self, xx):
        self.x = xx
        print('x좌표값이 %d로 변경되었습니다'%xx)
    def sety(self, yy):
        self.y = yy
        print('y좌표값이 %d로 변경되었습니다'%yy)
    def get(self):
        return (self.x, self.y)
    def move(self,dx,dy):
       self.x = x+dx
       self.y = y+dy
       print('변경된 x좌표값:%d,y좌표값:%d'%(dx,dy))

#문제 6-2
print('[문제 6-2]')

x=int(input('x좌표를 입력하십시오 :'))
y=int(input('y좌표를 입력하십시오 :'))
MyGPS = Point(x,y)

while 1:
    cho=input('기능을 선택하세요\n1 x좌표값 변경\n2 y좌표값 변경\n3 현재 좌표값\n4 좌표이동\n5 프로그램 종료(Enter any key)\n선택:')

    if cho == 1:
        MyGPS.setx(int(input('변경할 x좌표값을 입력하십시오:')))
    elif cho == 2:
        MyGPS.sety(int(input('변경할 y좌표값을 입력하십시오:')))
    elif cho == 3:
        a=MyGPS.get()
        print('현재 좌표값은 %d,%d 입니다'%(a[0],a[1]))
    elif cho == 4:
        dx=int(input("이동하실 좌표를 입력해주세요\nx:+"))
        dy=int(input("y:+"))
        MyGPS.move(dx,dy)
    else:
        break
print('프로그램 종료')
print('\n')

# 문제 6-3
print('[문제 6-3]')

class Stock:
    market = "kospi"

a = Stock()
b = Stock()

print('클래스 Stock 의 네임스페이스에는 market 라는 오브젝트가 포함되어 있다')
print(Stock.__dict__)
print('인스턴스 a, b의 네임스페이스에는 market 라는 오브젝트가 포함되어 있지 않는다')
print("a.__dict : ",a.__dict__)
print("b.__dict : ",b.__dict__)

print('\n')

# 문제 6-4
print('[문제 6-4]')

print('하지만 인스턴스에 호출하는 오브젝트가 없으면 해당 클래스에서 오브젝트를 받아온다')
print('a.market =',a.market)
print('b.market =',b.market)
print('Stock.market =',Stock.market)
print('\n')
print('인스턴스에 호출하는 오브젝트가 있으면 해당 클래스에서 오브젝트를 받아오지 않는다')
a.market = "nasdaq"
b.market = "nasdaq"
print('a.market =',a.market)
print('b.market =',b.market)
print('Stock.market =',Stock.market)

print('\n')
# 문제 6-5
print('[문제 6-5]')
print('클래스 Stock 의 네임스페이스에는 market 라는 오브젝트가 포함되어 있다')
print(Stock.__dict__)
print('인스턴스 a, b의 네임스페이스에는 market 라는 오브젝트가 포함되어 있으나 다른 값으로 정의를 하였기에 변수명만 같은 오브젝트이다 ')
print("a.__dict : ",a.__dict__)
print("b.__dict : ",b.__dict__)
print('id(stock.market) =',id(Stock.market))
print('id(stock.market)= ',id(a.market))
print('id(stock.market)= ',id(b.market))


# 문제 6-5
print('[문제 6-5]')


