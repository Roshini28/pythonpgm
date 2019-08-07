ae1=int(input())
bbe1=pow(2,ae1)
zee1=[]
for i in range(bbe1):  
    mee1=bin(i).replace("0b","")
    zee1.append(mee1.zfill(ae1))
    zee1.sort(key=(lambda x:x.count('1')))
for i in zee1:
    print(i)
