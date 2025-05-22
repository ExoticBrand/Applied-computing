#Challenge 34 - Area or perimeter

#This code would allow the uer to store a varible of the area
def out():
    area = length * width
    print("The area of the single face is ",area)
#This would ask for the users length width or height.
height = float(input("Please enter the height of your cuboid...: "))
length = float(input("Please enter the length of the cuboid...: "))
width = float(input("Please enter the width of the cuboid...: "))

out()
print("The volume of this cuboid is ... :",((length*width)*height))