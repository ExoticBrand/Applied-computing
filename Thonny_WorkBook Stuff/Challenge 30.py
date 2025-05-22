#Challenge 30

#This is a code that would require the person to add a name in and if they get it wrong they would ahve to repeat doing it until they get the question right.
Name = input("Please enter your name... : ")
while Name != "Sam":
        Name = input("Please try again the name starts with a S...: ")
print("Welcome Back ",Name)