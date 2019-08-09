def sub(aae1): 
    mmnt = len(aae1) 
    sub = [1]*mmnt 
    for j in range (1 , mmnt): 
        for i in range(0 , j): 
            if aae1[j] > aae1[i] and sub[j]< sub[i] + 1 : 
                sub[j] = sub[i]+1
    maximum = 0
    for j in range(mmnt): 
        maximum = max(maximum , sub[j])  
    return maximum
aar1=int(input()) 
aae1 = list(map(int,input().split()))
print (sub(aae1))
