#Challenge 20 - More advanced ways to use an if
choice = input("Please enter m or M...")
#if the varible is equal to M or m
if choice == "M" or choice == "m":
    print(choice)
    
ch0ice = input("Which team are you in? ")
#Makes the choice smaller into brakets
if ch0ice in("K","B"):
    print("We have a special offer of 10% off ferrets for students in B or K team")

#Shows that the brakets could extend to show more answers to print out if true.
voice = input("Which home group are you in? ")
if voice not in ("XB1","XB2","XB3","XB4","XK1","XK2","XK3","XK4"):
    print("Sorry you have not made a valid choice")