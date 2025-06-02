#Challenge 39 Part2
myFile = open("example.txt", "rt")
someone = [line.strip() for line in myFile]
for line in myFile:
    someone.append(line)

    weight1 = float(someone.pop())
    height1 = int(someone. pop())
    name1 = someone.pop()
    
    weight2 = float(someone.pop())
    height2 = int(someone. pop())
    name2 = someone.pop()
    
    weight3 = float(someone.pop())
    height3 = int(someone. pop())
    name3 = someone.pop()
    
    weight4 = float(someone.pop())
    height4 = int(someone. pop())
    name4 = someone.pop()
    
    weight5 = float(someone.pop())
    height5 = int(someone. pop())
    name5 = someone.pop()
    
    weight6 = float(someone.pop())
    height6 = int(someone. pop())
    name6 = someone.pop()
    
    print(f"Name = {name1}, Weight = {weight1}, Height = {height1}")
    print(f"Name = {name2}, Weight = {weight2}, Height = {height2}")
    print(f"Name = {name3}, Weight = {weight3}, Height = {height3}")
    print(f"Name = {name4}, Weight = {weight4}, Height = {height4}")
    print(f"Name = {name5}, Weight = {weight5}, Height = {height5}")
    print(f"Name = {name6}, Weight = {weight6}, Height = {height6}")

myFile.close()


