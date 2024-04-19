#Task 1 Food and Colour
'''color=input("Whatis your favourite colour?")
food=input("What is your favourite food?")
time=input("When do you need it - Breakfast, Lunch or dinner?")
print(f"You! I'll have {color} {food} for {time}")
'''

#Task 2

country=["Botswana","France","Germany","Hungary"]
capital=["Gaborne","Paris","Berlin","Budapest"]
#for i in range(0,len(country)-1):
ask=""
while True and ask!="Exit":
        num=int(input("enter the index value of the country"))
        if 0 <= num <= 3:
                print(capital[num])
                ask=input("Would you like to go ahead or Exit?")
        else:
                print("Sorry, wrong input. Index value must be between 0 and 3.")
                ask=input("Would you like to go ahead or Exit?")
        
        
                
        
                
        
 
