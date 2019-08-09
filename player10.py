c30,r28=map(str,input().split())
c30=list(c30)
r28=list(r28)
mmt=0
for h in range(0,len(c30)):
        if(c30[h]!=r28[h]):
            mmt=mmt+1
if(mmt==1):
    print("yes")
else:
    print("no")
