#Task 1 Food and Colour
'''color=input("Whatis your favourite colour?")
food=input("What is your favourite food?")
time=input("When do you need it - Breakfast, Lunch or dinner?")
print(f"You! I'll have {color} {food} for {time}")


#Task 2 Trivia Question done using lists

country=["Botswana","France","Germany","Hungary"]
capital=["Gaborne","Paris","Berlin","Budapest"]

ask=""
while True and ask!="Exit":
        num=int(input(
                "enter the index value of the country"))
        if 0 <= num <= 3:
                print(capital[num])
                ask=input("Would you like to go ahead or Exit?")
        else:
                print("Sorry, wrong input. Index value must be between 0 and 3.")
                ask=input("Would you like to go ahead or Exit?")
 '''       

#Section 4 Practice Task 1

while True:  # while loop to continue asking until a value is not between 1 to 4
        num=int(input("Enter a number between 1-4"))
        
        if num==1:
                print("uno")
        elif num==2:
                print("dos")
        elif num==3:
                print("tres")
        elif num==4:
                print("cuatro")
        else:
                print("I only know 1-4 in Spanish")
                break # if the value if more than 4 or less than 1 then end the program
                
        
                
        
 
