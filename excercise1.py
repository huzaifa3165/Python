# To add a number
print("What do you want to do:")
print("1. Add")
print("2. Multiply")
print("3. Divide")
print("4. Subtract")
myoperator=int(input())
while 1:
  if myoperator==1:
    a=int(input("Input first number"))
    b=int(input("Input second number"))
    print(a+b)
  if myoperator==2:
    
    a=int(input("Input first number"))
    b=int(input("Input second number"))
    print(a*b)
  if myoperator==3:
    
    a=int(input("Input first number"))
    b=int(input("Input second number"))
    print(a/b)
  if myoperator==4:
    
    a=int(input("Input first number"))
    b=int(input("Input second number"))
    print(a-b)
  else:
    print("Warning: Choose between 1 to 4!!")
