k=int(input())
s=0
for p in range(0,k):
  if(pow(2,p)>k):
    break
  s=k-pow(2,p)
print(s)

