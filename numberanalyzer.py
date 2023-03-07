name = input("Hello! What is your name? ")
number = int(input(name + ", Pick a number between 1 and 100 "))
while True :
    if number > 100 or number < 1:
        print("Your entry is invalid")
    if number % 2 == 1 and number <= 60:
        print("You entered " +str(number) +" and it is odd and less than 60")
    if number % 2 ==1 and number >= 60:
        print("You entered " + str(number) +" and it is odd and greater than 60")
    if number % 2 != 1 and number >= 2 and number <= 25:
        print("You entered " + str(number) + " and it is even and less than 25")
    if number % 2 != 1 and number >= 26 and number <= 60:
        print("You entered " + str(number) + " and it is even and between 26 and 60")
    if number % 2 !=1 and number >= 60:
        print("You entered " + str(number) + " and it is even and greater than 60")
    stop = input("Do you want to stop? y/n ")
    if stop.lower() == "y":
       break
    else:
        number = int(input(name + ", Pick a number between 1 and 100 "))
