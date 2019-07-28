m1,n1 = input().split()
m1,n1 = int(m1), int(n1)
Lt1 = [ int(x) for x in input().split()]
for i in range(0,n1) :
    a1,b1 = input().split()
    a1,b1 = int(a1), int(b1)
for i in range(0,n1):
    print(min(Lt1[a1-1:b1]))
