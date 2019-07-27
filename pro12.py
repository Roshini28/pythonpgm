m1,r1=list(map(int,input().split()))
lis1=list(map(int,input().split()))
for i in range(r1):
  u1,v1=list(map(int,input().split()))
  print(sum(lis1[u1-1:v1]))
