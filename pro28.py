aae1=int(input())
bbe1=[int(snt) for snt in input().split()]
bbe1.sort()
snt=0
xmt=0
for j in range(len(bbe1)):
    if bbe1[j]>=snt:
        xmt+=1
    snt=snt+bbe1[j]
print(xmt)
