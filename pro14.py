n11,n12=list(map(int,input().split()))
lit1=list(map(int,input().split()))
lit2=[]
while(n12):
	k1 = list(map(int,input().split()))
	lit2.append(k1)
	n12-=1
for ic in lit2:
	val=0
	for jc in range(ic[0]-1,ic[1]):
		val=val^lit1[jc]
	print(val)
