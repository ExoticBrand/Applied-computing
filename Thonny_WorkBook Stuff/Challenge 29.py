# Challenge 29 - While loops

#This would keep repeating the same question in line 6 till the user would input a number between 1 and 10
number = 100
while number > 10 or number < 0:
    number =int(input("Please enter a number between 1 and 100 : "))
print("Your number multiplied by 10 is:",number*10)