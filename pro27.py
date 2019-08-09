aae1,bbe1=map(int,input().split())
cce1=list(map(int,input().split()))
peq=list(map(int,input().split()))
qep=[]
annt=0
for i in range(aae1):
    xt=peq[i]/cce1[i]
    qep.append(xt)
while bbe1>=0 and len(qep)>0:
    mindex=qep.index(max(qep))
    if bbe1>=cce1[mindex]:
        annt=annt+peq[mindex]
        bbe1=bbe1-cce1[mindex]
    cce1.pop(mindex)
    peq.pop(mindex)
    qep.pop(mindex)
print(annt)
