def val():
  print("1.current\n2.saving")
  a=int(input())
  if(a==1):
    opt(1)
  elif(a==2):
    opt(2)
  else:
    new()   
    val()

def new():
  print("Invalid data")
  
  
def valid():
  name=input("enter the name:")
  pin=input("enter your pin:")  
  if (name=='roshi' and pin=='1234'):
    print("\nWelcome",name)
    val()
  elif(name=='roshi'):
    print("Enter valid PIN")
    valid()
  elif(pin=='1234'):
    print("Enter valid Name")
    valid()
  else:
    print("Invalid Name and Pin")
    valid()
  

def opt(x):
  print("\n1.Deposit\n2.Withdraw\n3.Balance enquiry")
  opt2(int(input()))

def opt2(x):
  if(x==1):
    deposit()
  elif(x==2):
    withdraw()
  elif(x==3):
    balenq()
  else:
    new()  
    opt(x)

def opt3(y):
  if(y==1):
    opt(y)
  elif(y==0):
    print("Thank you for visiting")
  else:
    new()
    opt2(x)

def con():
  print("if you want to countinue press1\nto exit press0")
  opt3(int(input()))

def deposit():
  print("enter the amount to be deposited:")
  dep=int(input())
  if(dep>=1000):
    val=dep+money
    print("amount deposited:",dep)
    print("current amount:",val)
  else:
    print("deposit above 1000rs") 
    deposit()
  con()  

def withdraw():
  print("enter the amount to be withdraw:")
  dep=int(input())
  if(money<dep):
    print("insuffient balance")
  elif(dep<500):
    print("enter the amount above 500rs")
    withdraw()  
  else:
    val=money-dep
    print("amount withdraw:",dep)
    print("current amount:",val)
  con()
  
def balenq():
  print("your current balance is:",money)
  con()
 

money=5000
valid()
