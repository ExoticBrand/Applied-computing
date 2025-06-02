#BRANDON NGUYEN SAC : CLASS ATTENDANCE REPORT

#BEGIN

#This would put a varible into a dictionary for later purposes
def dictionary_adder(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = value
student_ID = {}

#User would import some imformation about their total amount of students and the amount of periods in the week.
#Ask user for periods in week (0-5)
TotalStudents = int(input("Please enter the total amount of students in the classroom..."))
#If total periods < 0 and total periods < 5
TotalPeriodsInWeek = int(input("Please enter the total amount of periods held in this week (1 to 5)..."))

#Checks TotalPeriodsInWeek if it is below or equal to 5 and if its greater than 5 then it would output "Invalid".
#If total periods < 0 and total periods < 5
if TotalPeriodsInWeek > 5 and TotalPeriodsInWeek < 0:
    #Invalid answer please enter between 0 - 5..
    TotalPeriodsInWeek = int(input("This is an invalid answer please try again..."))

#Varibles : This is where some varibles would come in handy for purposes
LiterallyZero = 1 #This would allow the code to repeat till it equals to the TotalPeriodsInWeek.
Periods = 1       #This would show the period in the print statements
ID = 1            #This would allow the number in the attendance to go up after another line.
no = "No"         #NEED TO REMOVE THIS
COUNTERA = 0      #This would allow the code to count the amount of absents that the student would have.(It would depend on what the user inputs)
COUNTERP = 0      #This would allow the code to count the amount of present's that the student would have.(It would depend on what the user inputs)


#This is when the code would get tricky... This would repeat until the demand from the user input would be equal to what the user inputs.
#Repeats the code depending on the Total students
for Something in range (1,TotalStudents + 1):#Repeats the Whole paragraph
    #Ask user for their student name
    Student1 = input(f"Please enter name of Student {ID}: ") #Allows the user to add a name to the student.
    #SPACE
    print(" ") #Extra space
    #Repeats the code depending ont eh amount of periods
    for Number in range (Periods, Periods+TotalPeriodsInWeek):#If the certain amount is less than the user import they would continue printing
        #Ask user if student name is present or Absent (P/A)
        PresentOrAb = input(f"Enter attendance for {Student1} (P/A) for period {Periods}: ")
        
        
#Converts the PresentOrAb to a uppercase.
        PRESENTORAB = PresentOrAb.upper()
#This would read how many P or A did the user input and add "1" to the COUNTERA & COUNTERP if true
        #(P/A) is equal to “P”:
        if PRESENTORAB == "P":
            #Plus one to COUNTERP
            COUNTERP += 1
        #(P/A) is equal to “A”:
        elif PRESENTORAB == "A":
            #Plus one to COUNTERA
            COUNTERA += 1

#This would check if the user import is not P or A it would ask them to try again
        #Else
        if PRESENTORAB != "P" and PRESENTORAB != "A":
            #Redo PresenterAB because the import is invalid
            PRESENTORAB= input(f"Sorry that is invalid... Please enter (P/A) for {Student1} for period {Periods}: ")
            
#Periods would have the hardest time out of all the rest of the varibles because of how much it requires attention...
        #Periods plus one 
        Periods += 1
        
#This would allow the code to keep on repeating till the value of LiterallyZero reaches the same calue as Total Students
    #LiterallyZero plus one
    LiterallyZero += 1
    
#Allows the stundet number in import in ID to stack up from 1 to whatever the user input would be.
    #ID plus one
    ID = ID + 1
    
#This would allow the counter's to convert the A & P into a fraction that would be printed in the following statements.
#Round would round the decimal to the closest whole number.
    #Counterp would be rounded up to a percentage and into an integer
    Counterp = round((COUNTERP / TotalPeriodsInWeek)* 100 ,2)
    #Countera would be rounded up to a percentage and into an integer
    Countera = round((COUNTERA / TotalPeriodsInWeek)* 100 ,2)
    
#This would then add the varibles collected by the inputs and store them into dictonary
    #Dictionary would import studentID,Name and counterp
    dictionary_adder(student_ID, Student1, Counterp)

#Prints out the results
    #Prints name and percentage of P’s & A’s
    print(f"{Student1}'s Total amount of Present = {COUNTERP}, And Absents = {COUNTERA}\n")
#This would then write down the results into a document and save it from there
    #Writes in file and saves the same print (Prints name and percentage of P’s & A’s)
    with open ("example.txt", "wt") as file:
        file.write(f" {Student1}'s Total amount of Present = {COUNTERP}, And Absents = {COUNTERA}\n")
        
#This part would reset everything back to the beginning to start the process again.
    #COUNTERP would be saved back into the value of 0
    COUNTERP = 0
    #COUNTERA would be saved back into the value of 0
    COUNTERA = 0
    #Periods would reset into 1
    Periods = 1
    
    
    
#This would then collect the information collected from the questions/attendance and print out what and the Warning for the lowest attendence.
#Prints out Attendance report as a title
print("\nAttendance Report:")


#Observes the percentage if its less than 50% or else. And prints out their results
#Opens the Write file and splits the Name and Percentages from the file
for name, percentages in student_ID.items():
    
#This would convert the percentages into an int with no decimal number
    #Converts percentage to integer
    percentages = int(percentages)
    
#If the percentages is less than 50 then it would print "Warning Low Attendance"
    #If the percentage is less than 50%
    if percentages <= 50:
        #Prints Warning message with the original print(Name and Percentage)
        print(f"Student Name : {name}, Stundets Attendance Report : ({percentages}%) - Warning Low Attendence")
        
#If the student has a percentages on their presents = 100%
    #If percentage is greater than 50 
    elif percentages == 100:
        #Prints nothing added with print(Name and Percentage)
        print(f"Student Name : {name}, Stundets Attendance Report : ({percentages}%) - Amazing Attendance")

#If the percentages is greater than 50 it would print out a regular out put.
    #Other import
    else:
        #Prints out congrats on a 100% attendance.
        print(f"Student Name : {name}, Stundets Attendance Report : ({percentages}%)")

#Just in case if it is required to be printed because its in the example.
#Prints out a line in the document (Data written to file)
print("\nData written to file.")

#END














