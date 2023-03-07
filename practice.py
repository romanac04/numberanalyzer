while True:
    print("Hello World!")
    response = input("Would you like to continue? (y/n) ")
    if response == "n":
        print("Goodbye!")
        break

while True:
    number = int(input("Enter a number. "))
    for i in range(number):
        print(i)
    for number in range(number-1, -1, -1):
         print(number)
    response = input("Would you like to continue? (y/n) ")
    if response == "y":
            number = int(input("Enter a number. "))
            for i in range(number):
                print(i)
            for number in range(number - 1, -1, -1):
                print(number)

    if response == "n":
        print("Goodbye!")
    break