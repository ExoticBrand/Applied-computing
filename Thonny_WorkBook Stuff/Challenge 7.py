#Challenge 7
#Asking the user to enter their length & width of their room in metres
Length =float(input("Please enter the length of your room in metres: "))
Width = float(input("Please enter the width of your room in metres: "))
#Times the length & width together
Area = (Length*Width)
print("Your carpet requires ",Area,"m² to fill the whole floor up with carpet")

#Challenge 8
#Shows the how old you are and their name
Name = input("Please enter your name :")
Age = int(input("Please enter how old you are: "))
Days = Age*365
Hours = Days*24
Min = Hours*60
print("You have lived for ",Days," days")
print("You have lived for ",Hours," hours")
print("You have lived for ",Min," minutes")
print("You have lived for ",Min*60," seconds")