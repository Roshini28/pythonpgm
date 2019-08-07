pe1=int(input())
qe1=list(map(int,input().split()))
qe1.sort()
qe1.reverse()
if qe1[0]==0:
    print(0)
else:
    for j in qe1:
        print(j,end='')
