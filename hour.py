numbr=int(input())
j=0
if(numbr<60):
  print(0,numbr)
else:
  while(numbr>=60):
    numbr=numbr-60;
    j=j+1
  print(j,numbr)
