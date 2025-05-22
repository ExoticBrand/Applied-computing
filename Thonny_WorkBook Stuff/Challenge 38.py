#Challenge 38 - Writing  program that prints out stuff in wordpad
myFile = open ("example.txt", "wt")
#This is where the user would import their varibles

num1 = input("Please enter a random number...: ")
num2 = input("Please enter another random number...: ")
num3 = input("Sorry for asking again BUT could you enter ANOTHER random number...: ")
num4 = input("Enter another random number...: ")
num5 = input("Enter your final random number...: ")
num6 = input("Enter your LAST random number...: ")
#THe varibles that the user imported would be listed in the List[]
List = [ num1, num2, num3 , num4 , num5, num6]
for item in List:
    myFile.write(item+"\n")
myFile.close()

#This would open up the myFile again and it would print out the context.
myFile = open ("example.txt", "rt")
contents = myFile.read()
print (contents)
myFile.close()


