aae1=input()
a28=list(map(int,aae1.split()))
m3=a28[1]
he1=input()
flag=0
se1=list(map(int,he1.split()))
for i in range(0,len(se1)-1):
	for j in range(i+1,len(se1)):
		if se1[i]+se1[j]==m3:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
