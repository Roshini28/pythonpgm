aae1 = int(input())
bbe1 = int(aae1/2)
cce1 = []
for j in range(aae1, bbe1, -1):
    i = str(j)
    if j + sum([int(dde1) for dde1 in i]) == aae1:
        print(1)
        print(j)
        break
else:
    print(0) 
