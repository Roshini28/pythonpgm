aae1=input()
lae1=list(map(int,input().split()))
max=0
j=0
while(j<len(lae1)-1):
    count=0
    while(j<len(lae1)-1 and lae1[j]<lae1[j+1]):
        count+=1
        j+=1
    if(count>max):
        max=count
    j+=1
print(max+1)
