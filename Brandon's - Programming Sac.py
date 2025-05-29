#BRANDON NGUYEN SAC : CLASS ATTENDANCE REPORT

#This would put a varible into a dictionary for later purposes
def dictionary_adder(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = value
student_ID = {}

#User would import some imformation about their total amount of students and the amount of periods in the week.
TotalStudents = int(input("Please enter the total amount of students in the classroom..."))
TotalPeriodsInWeek = int(input("Please enter the total amount of periods held in this week (1 to 5)..."))

#Checks TotalPeriodsInWeek if it is below or equal to 5 and if its greater than 5 then it would output "Invalid".
if TotalPeriodsInWeek > 5 and TotalPeriodsInWeek < 0:
    TotalPeriodsInWeek = int(input("This is an invalid answer please try again..."))

#Varibles : This is where some varibles would come in handy for purposes
LiterallyZero = 1 #This would allow the code to repeat till it equals to the TotalPeriodsInWeek.
Periods = 1       #This would show the period in the print statements
ID = 1            #This would allow the number in the attendance to go up after another line.
no = "No"         #NEED TO REMOVE THIS
COUNTERA = 0      #This would allow the code to count the amount of absents that the student would have.(It would depend on what the user inputs)
COUNTERP = 0      #This would allow the code to count the amount of present's that the student would have.(It would depend on what the user inputs)


#This is when the code would get tricky... This would repeat until the demand from the user input would be equal to what the user inputs.
for Something in range (1,TotalStudents + 1):#Repeats the Whole paragraph
    Student1 = input(f"Please enter name of Student {ID}: ") #Allows the user to add a name to the student.
    
    print(" ") #Extra space
    for Number in range (Periods, Periods+TotalPeriodsInWeek):#If the certain amount is less than the user import they would continue printing
        PresentOrAb = input(f"Enter attendance for {Student1} (P/A) for period {Periods}: ")
        
        
#Converts the PresentOrAb to a uppercase.
        PRESENTORAB = PresentOrAb.upper()
#This would read how many P or A did the user input and add "1" to the COUNTERA & COUNTERP if true
        if PRESENTORAB == "P":
            COUNTERP += 1
        elif PRESENTORAB == "A":
            COUNTERA += 1

#This would check if the user import is not P or A it would ask them to try again
        if PRESENTORAB != "P" and PRESENTORAB != "A":
            PRESENTORAB= input(f"Sorry that is invalid... Please enter (P/A) for {Student1} for period {Periods}: ")
            
#Periods would have the hardest time out of all the rest of the varibles because of how much it requires attention...
        Periods += 1
        
#This would allow the code to keep on repeating till the value of LiterallyZero reaches the same calue as Total Students
    LiterallyZero += 1
    
#Allows the stundet number in import in ID to stack up from 1 to whatever the user input would be.
    ID = ID + 1
    
#This would allow the counter's to convert the A & P into a fraction that would be printed in the following statements.
#Round would round the decimal to the closest whole number.
    Counterp = round((COUNTERP / TotalPeriodsInWeek)* 100 ,2)
    Countera = round((COUNTERA / TotalPeriodsInWeek)* 100 ,2)
    
#This would then add the varibles collected by the inputs and store them into dictonary
    dictionary_adder(student_ID, Student1, Counterp)

#Prints out the results
    print(f"{Student1}'s Total amount of Present = {COUNTERP}, And Absents = {COUNTERA}\n")
#This would then write down the results into a document and save it from there
    with open ("example.txt", "wt") as file:
        file.write(f" {Student1}'s Total amount of Present = {COUNTERP}, And Absents = {COUNTERA}\n")
        
#This part would reset everything back to the beginning to start the process again.
    COUNTERP = 0
    COUNTERA = 0
    Periods = 1
    
#This would then collect the information collected from the questions/attendance and print out what and the Warning for the lowest attendence.
print("\nAttendance Report:")

#Observes the percentage if its less than 50% or else. And prints out their results
for name, percentages in student_ID.items():
    percentages = int(percentages)
    if percentages <= 50:
        print(f"Student Name : {name}, Stundets Attendance Report : ({percentages}%) - Warning Low Attendence")
    else:
        print(f"Student Name : {name}, Stundets Attendance Report : ({percentages}%)")

#Just in case if it is required to be printed because its in the example.
print("\nData written to file.")
#END














