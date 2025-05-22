#Challenge 6
#This would ask for steves calories
print("Steve's calorie counter")
calories =int(input("How many calories have you eaten today? "))
#Number 2000 is the limited amount of calories you can eat.
s=2000-calories
print("You can eat ",s," more calories today")

#Challenge 6's Challenge...
#This would ask for how much cash did someone spend during school lunch
LunchComsumed = float(input("Please enter the amount spent on school lunch " ))
#Asking for the amount of cash at the start of the day
Money = float(input("Please enter the amount of cash you had durign the start of the day" ))
#Shows how much cash lost
if Money-LunchComsumed<=0:
    print("Your broke now..")
    
else:
    print(Money-LunchComsumed)
    
            