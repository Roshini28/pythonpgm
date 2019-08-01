aprt,brt=map(int,input().split())
l1=[]
for _ in range(aprt):
    l1.append(input())
for ic in range(len(l1)):
    if('0' in l1[ic]):
        l1[ic]=l1[ic].replace('0','')
    l1[ic]=l1[ic].replace(' ','')
lengths=[]
for ic in l1:
    if(len(ic)>0):
        lengths.append(len(ic))
brt=min(lengths)
r1='1 '*brt
r1=r1.strip()
for ic in range(brt):
    print(r1)
