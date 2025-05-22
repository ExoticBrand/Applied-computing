#Challenge 18 & 19-If..
#If statements to have endless outcomes...
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#This would print out different outcomes depending on the input the user adds in
if num1>num2:
    print(num1," Is greater than",num2)
    
if num1 <num2:
    print(num2," Is greater than",num1)
    
if num1 == num2:
    print(num1," Is equal to ",num2)
#A different way to print out the code knowing it would result in the same outcome.
if num1>num2:
    print(num1," Is greater than",num2)
    
elif num1 <num2:
    print(num2," Is greater than",num1)
    
else:
    print(num1," Is equal to ",num2)

