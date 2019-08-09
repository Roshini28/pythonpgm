chen=(input())
kpm=0
for k in range(0,len(chen)):
    vsi=(chen[:k]+chen[k+1:])
    if(int(vsi) % 8==0):
        kpm=1
        break
if(kpm==1):
    print("yes")
else:
    print("no")
