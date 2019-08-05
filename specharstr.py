roe=input()
ros=0
for i in range(len(roe)):
  if(roe[i].isdigit() or roe[i].isalpha() or roe[i]==(" ")):
    continue
  else:
    ros+=1
print(ros)
