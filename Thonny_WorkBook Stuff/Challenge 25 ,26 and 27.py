#Challenge 25, 26 and 27
#Challenge 25 - For Loops
#Repeats the certain for code until the task is complete
a = int(input("Please enter a number between 0 & 10 : "))
#This code would be different to the certain amount of for programs...
#Instead of doing for a in range(10) and repeating it till the value hits 10 it would plus the value 2 till it hits its target 
for a in range(1,11,2):
    print(a)
    
#Challenge 26 - For loops
    #This would add 5 to the value of b till the value would hit 100.
b = int(input("Please enter a number between 10 to 100...: "))
for b in range(10,100,5):
    print(b)
    
#Challlenge 27 -Times Table using For loops
sentence = "here is a sentence. How many letter 'e''s are there in it?"
number3 = 0

for letter in sentence:
    if letter == "e":
        number3 +=1
print("The number of e's in the sentence is: ",number3)
