name = input("Type your name:")
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go?")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim acorss? type walk to walk around or swim")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print('Not a valid option. You lose')
elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross or head back")
else:
    print('Not a valid option. You lose')