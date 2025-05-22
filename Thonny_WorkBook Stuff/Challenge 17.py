#Challenge 17 -Magic 8 Ball
#This would add the random varible to the whole code
import random
#Answers whenever it guesses.
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")

print("Welcome to the Magic 8 Ball game - use it to answewr your questions..")

question = input("Ask me for any advice and i'll help you out. Type in your question then press Enter for an answer.")

print("shaking....\n"*4)

cho1ce = random.randint(5,7)
#Print out something random.
if cho1ce == 1:
    answer=answer1
elif cho1ce ==2:
    answer=answer2
else:
    answer=answer3
    
print(answer)