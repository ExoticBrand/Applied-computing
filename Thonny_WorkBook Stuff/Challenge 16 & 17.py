import random
#Challenge 15 & 16

#Challenge 15 - Formating numbers with decimals.
#Varibles times together without decimal.
nOne = 3.123456789
nTwo = 9.87654321
ans = (nOne*nTwo)
print(ans)

#This code would round up the code (Sady the second code didnt work..)
print("%0.3f"%(ans))

#Challenge 16 - Restaurant Tip
#Asking how much people would like to pay
People = int(input("Please enter how much people would like to pay : "))
includingTIP = 100*1.15
InTheEnd = includingTIP/People
Total = ("%0.3f"%(InTheEnd))
print(f"Each person could pay up to {Total}$ each including tip")
