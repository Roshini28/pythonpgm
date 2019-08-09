a28= []
def drime(o):
    c3 = 0
    for x in range(2,o-1):
        if o%x == 0:
            c3 =1
            break
    if not c3:
        a28.append(o)

r2 ,chan3 = map(int,input().split())

for h1 in range(r2,chan3+1):
    drime(h1)
print(len(a28))
