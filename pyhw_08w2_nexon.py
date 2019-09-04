# 8월 2주차

# 과제(1)
print('과제(1):')
def gen(n):
    x = n
    while x>0:
        n += x%10
        x//=10
    return n
A=set(range(1,5000))
B=set(gen(n)for n in range(1,5000))
print(sum(A-B))

print('\n')

# 과제 (2)
print('과제(2):')

X = {n for n in range(1,1000)}
Y = {n*3 for n in X}
Z = {n*5 for n in X}
print(X-Y-Z)
print(sum(X-Y-Z))
