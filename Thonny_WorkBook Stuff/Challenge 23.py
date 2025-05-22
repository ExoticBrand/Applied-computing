#Challenge 23 - Mobile Phone Cost
#This would caculate how much they would pay for a certain amount of mb
pics = int(input("Please enter the amount of picture you took...:"))
text = int(input("Please enter the amount of text you have sent...:"))
MB = float(input("Please enter the amount of MB you have on your mobile device...:"))
#Caculates the total amount of cost
caculation = (pics*0.35)+(text*0.10)+(MB*0.05)
if caculation >10:
    #This caculation would result in the customer paying more than 10$ from their mobile cost
    print("Make sure to focus less on your device!")
else:
    print("Your fine...")