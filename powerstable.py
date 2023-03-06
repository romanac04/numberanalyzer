
print("Enter a integer below.")
number = int(input())
print("Number\tSquare\tCube")
while True:
    for i in range(1, number + 1 ):
        square = i ** 2
        cube = i ** 3
        print(str(i) + "       " + str(square) + "       " + str(cube))
    response = input("Continue? y/n ")
    if response.lower() == "n":
        break
    else:
        print("Enter a integer below")
        number = int(input())

for j in range (1,11):
    row =" "
    for k in range (1,11):
        row += str(j*k) + " "
    print(row)
