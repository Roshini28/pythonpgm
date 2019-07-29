ntn1=int(input())
l1=list(map(int,input().split()))
a1=[1]*ntn1
for dt in range(ntn1):
    if(dt==0):
        if(l1[dt]>l1[dt+1]):
            at[dt]=at[dt]+at[dt+1]
    elif(dt>0):
        if(l1[dt]>l1[dt-1]):
            a1[dt]=a1[dt]+a1[dt-1]
print(sum(a1))
