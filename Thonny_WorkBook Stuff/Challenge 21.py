#Challenge 21 - Mega Sale
#THis program would see if the customer would get a voucher for their next purcahse
Spent = float(input("Please enter how much you spent on a local shop :"))
#If statement if their customer would spent >20 or >10 money.
if Spent >= 20:
    print("Congrats you earned yourself a $3 voucher for the your next purchase!")
elif Spent >= 10:
    print("Congrats you earned yourself a $1 voucher!")
else:
    print("You get no voucher...")