#Challenge 32 - Making a times table (Using Nested for loops)
#Repeats the table until it does the maximum of 12x12
for i in range(1,13):
    print(i, "Times table\n")
    for j in range(1,13):
        print(i, "Times",j,"=",i*j)

#This would times the numer till it hits 24 and repeat till the first digit would reach before 25 starts.
for e in range(1,25):
    print(e,"Times table\n")
    for r in range(1,25):
        print(e,"Times",r,"=",e*r)