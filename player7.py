a28=list(input())
b30=len(a28)
new=''
for k in range (0,b30,2):
    a28[k],a28[k+1]=a28[k+1],a28[k]
print(*a28,sep='')
