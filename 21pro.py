nn1=int(input())
ll1=list(map(int,input().split()))[:nn1]
div=int(nn1/2)
aa1=sum(ll1[:div])//len(ll1[:div])
aa2=sum(ll1[div:])//len(ll1[div:])
if(aa1==aa2):
  print("yes")
else:
  print("no")
