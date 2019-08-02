size8=int(input())
arr3=[]
for j in range(size8):
	dt=input()
	dt=list(map(int,dt.split(" ")))
	nt=len(dt)
	for i in range(nt):
		arr3.append(dt[i])
arr3.sort()
print(*arr3,sep=" ")
