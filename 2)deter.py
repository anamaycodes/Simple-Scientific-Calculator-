print("Program To find determinant of numbers")
p=str(input("how much size of matrix is needed?(Eg-'2x2') "))
if p=="2x2":
    print("[a11 a12]")
    print("[a21 a22]")
    a=int(input("Enter a11 number "))
    b=int(input("Enter a12 number "))
    c=int(input("Enter a21 number "))
    d=int(input("Enter a22 number "))
    x = a*d
    y = b*c
    z = x-y
    print("|",a," ",b,"|")
    print("|",a," ",b,"|")
    print("The determinant of above question is", z) 
    print("The program will Automatically Reseted. To Terminate the progrme type 'exit'")
  elif p=="exit":
    print("program terminated")
    break
  elif p=="3x3":
    print("Sorry, We have only 2x2 size available right now")   
else:
  print("Error 401")    
exit()
