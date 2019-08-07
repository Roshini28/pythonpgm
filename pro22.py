aannt=int(input())
aae1=list(map(int,input().split()))
pe1=[]
qe1=[]
for i in range(len(aae1)):
	if i%2==0:
		pe1.append(aae1[i])
	else:
		qe1.append(aae1[i])
se1=sum(pe1)
re1=sum(qe1)
if(se1>re1):
	print(se1)
else:
	print(re1)
