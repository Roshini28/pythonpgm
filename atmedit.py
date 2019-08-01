username=input("enter your username:")
pin=input("enter your pin:")
blnc=6000

list=["roshi",'1234']
if(username and pin in list):
  print("welcome roshi!!")
  print("1.current account\n 2.savings account")
else:
  print("sorry,invalid user")
c=int(input())
if(c == 1):
  print("1.withdraw\n 2.deposit\n 3.blnc enquiry")
elif(c == 2):
  print("1.withdraw\n 2.deposit\n 3.blnc enquiry")
else:
  print("invalid")
c=int(input())
if(c == 1):
    amt=int(input("enter your amt:"))
    if(amt<6000):
      print("collect your amt")
      blnc=blnc-amt
      print("blnc:rs.",blnc)
      print("thank you for your visiting!!")
    else:
      print("insuf blnc")
elif(c==2):
  amt1=int(input("enter your amt:"))
  blnc=blnc+amt1
  print("blnc:rs:",blnc)
  print("thank you for your visiting!!")

  
elif(c == 3):
  print("blnc:rs:",blnc)
  print("thank you for your visiting!!")

elif(c==0):
    print("thank you!!")
else:
  print("invalid")
  




