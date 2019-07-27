a1=int(input())
b1=0
l1=[]
for i in range(1,a1+1):
  l1.append(i)
for i in range(len(l1)):
  for i in range(i+1,len(l1)):
    b1+=1
print(b1)
