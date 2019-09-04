#행렬 집합 c
#행렬가로 길이 a
#행렬세로 길이 b
#라운딩 수행횟수 lt
#라운딩 좌표 t
#행렬원소 1~a*b-1
#결승 skt 


def ray(a,b):
    c = [0 for _ in range(b)]
    for p in range(b):
        c[p] = [0 for _ in range(a)]
    token=-1
    lt=((a*b-1)+a+b+1)//4
    for t in range(lt):
        skt=t//4
        if t%4==0:
            for i in range(1,a-skt):
                if c[0+skt][i-1+skt]==0:
                    token=token+1
                    c[0+skt][i-1+skt]=token
            print("첫번째token:",token,"라운딩:",skt)
        elif t%4==1:
            for i in range(1,b-skt):
                if c[i-1+skt][a-1-skt]==0:
                    token=token+1
                    c[i-1+skt][a-1-skt]=token
            print("두번째token:",token,"라운딩:",skt)
        elif t%4==2:
            for i in reversed(range(1,a-skt)):
                if c[b-1-skt][i]==0:
                    token=token+1
                    c[b-1-skt][i]=token
            print("세번째token:",token,"라운딩:",skt)
        elif t%4==3:
            for i in reversed(range(1,b-skt)):
                if c[i][0+skt]==0:
                    token=token+1
                    c[i][0+skt]=token
                else:
                    print("끝맺음성공적")
                    t=lt-1
            print("네번째token:",token,"라운딩:",skt)
    for i in range(b):
        print(c[i])

ray(6,6)
