i = 0
while True:
    i += 1
    if i < 11:
        print(i)
    else:
        break
j = 11
while True:
    j -= 1
    if j > 0:
        print(j)
    else:
        break
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

string = input("Enter a string ")
length = len(string)
if length < 10:
    print(length)
    added_space = 10 - length
    for i in range(length):
     i = " " * added_space
    print(i + string)
