#Challenge 3 , 4 , 5

#Challenge 3
#Asking the user to input two numbers between 0 & 10
numberOne =input("Enter a number between 0 & 10 ")
numberTwo =input("Enter another number between 0 & 10 ")
#This would print out the number next to another number instead of adding eachother
print(numberOne+numberTwo)

#Challenge 4
#We add an int infront of the whole code to allow the device to identify the input as a number
NumberOne = int(input("Please enter a number between 0 & 10 "))
NumberTwo = int(input("Please enter another number between 0 & 10 "))
#Prints out the new output as the numbers inputed added up
#However if you add numbers with a decimal it would have an error
print(NumberOne+NumberTwo)
                
#Challenge 5
#To fix this you need to add float to allow the device to see decimals as well
NUMBEROne = float(input("Please enter a number between 0 & 10 "))
NUMBERTwo = float(input("Please enter another number between 0 & 10 "))
#Outputs the two inputed numbers added up.
print(NUMBEROne+NUMBERTwo)