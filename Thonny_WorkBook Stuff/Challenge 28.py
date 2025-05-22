#Challenge 28 - Reading a sentence

#This would print out how much vowels are there inside this sentence
Quote =input("Please enter a random sentence :")
awa = 0


for letter in Quote:
    #This would then see how much vowels there are and if its true it would add one to another varible to print out the number of vowels.
    if letter in ("a" , "e" , "i" , "u" , "o"):
        awa += 1
        
print("The number of vowel in this sentence is: ",awa)