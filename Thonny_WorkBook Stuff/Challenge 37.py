#Challenge 37 - Creat a dictionary????

#This varible would allow me to convert the 
countrypop = {"Japan":127000000,"Germany":81000000,"Iran":77000000,"UK":64000000,"Canada":33000000,"Australia":23000000,"USA":317000000,"Bulgaria":7000000,"Sweden":1000000}
#Asking for the users choice
countryuno = input("Please enter a country between Japan, Germany, Iran, UK, Canada, Australia, USA, Bulgaria or Sweden...")
countryduo = input("Please enter a second country between Japan, Germany, Iran, UK, Canada, Australia, USA, Bulgaria or Sweden...")
#This part would then convert the users choice into lowercase.
countryuuno = countryuno.lower()
countrydduo = countryduo.lower()
#This would then convert the first digit from the lowercase form of the users choice to an uppercase.
capitalized_countryuuno = countryuuno.capitalize()
capitalized_countrydduo = countrydduo.capitalize()
#This would scan the countrypop and convert the string into a number that allows me to add thenm together
populationUS = countrypop[capitalized_countryuuno]+countrypop[capitalized_countrydduo]
print("The coutnry you have imported is...",capitalized_countryuuno," & ",capitalized_countrydduo,".")
print("Their population added together would equal to...",populationUS,"\n")