#Challenge 39 - People list (Issues)
#for item in END:
    #Name, Height, Weight = END
    #print(f"Name = {Name}, Height ={Height}, Weight ={Weight}")
myFile = open ("example.txt", "wt")
List = [ ('James', 73, 1.82), ('Peter', 78, 1.80), ('Jay',0,0), ('Beth', 65, 1.53), ('Mags', 66, 1.50), ('Joy',62 ,1.34)]
for someone in List:
    name, weight, height = someone
    print(f"Name = {name}, Weight = {weight}, Height = {height}")
myFile.close()
            

