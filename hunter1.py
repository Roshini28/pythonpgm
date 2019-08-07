try:
	ne1=int(input())
	array=list(map(int,input().split()))
	pae1=[]
	for j in array:
		if array.count(j)>1:
			if j not in pae1:
				pae1.append(j)
	print(*pae1)
	if len(pae1)==0:
		print("unique")
except ValueError:
	print("invalid")
