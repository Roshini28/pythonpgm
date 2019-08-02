nt,mt=list(map(int,input().split()))
l1=list(map(int,input().split()))
l1.sort(reverse=True)
c1=0
for i in l1:
    if mt==0:
        break
    q1=mt // i
    c1+=q1
    mt=mt-i*q1
print(c1)
