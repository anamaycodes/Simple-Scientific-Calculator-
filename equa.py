print("Enter the number in the following, for joint equation")
pair1=str(input("Enter the number before x "))
pair2=str(input("Enter the number before y "))
sign=str(input("Enter the sign between x,y"))
if "-" in pair2 and "+" in sign:
  print("Your above equation is: ",pair1,"x","-",pair2,"y=0")
elif "-" in pair2 and "-" in sign:
  print("Your above equation is: ",pair1,"x",sign,"(",pair2, "y ) = 0")

else:
  print("Your above equation is: ",pair1,"x",sign,pair2,"y = 0")
exit()


  
