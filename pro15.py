at=int(input())
bt=list(map(int,input().split(" ")))
bt=[bin(j) for j in bt]
bt.sort(reverse=True)
bt=[int(at,2) for at in bt]
for i in range(0,at):
     print(bt[i])
