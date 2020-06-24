#Take value from user for operation
print("What do you want to do from above operation?('Enter the number for operation selelction')")
print("1)Simple Calculator:Addition,Subtraction,Multiplication,Division")
print("2)To find determinent")
print("3)To find Slope")
print("4)To find Addition of two vector")
print("5)To display Equation of line")
print("6) To find greates number of two")
lol=int(input())
if lol==1:
  import simple.py
elif lol==2:
  import deter.py
elif lol==3:
  import slope.py
elif lol==4:
  import vector.py
elif lol==5:
  import equa.py   
elif lol==6:
  import great.py  
else:
  print("INVALID ENTERY.") 

