print("Bim Bum Bam!!")

name = input("What's your name? ").upper()
age = int(input("What's your age? "))

print("Hello", name, "you are", age, "years hold.")

points = 10

if age >= 18:
    print("Hooray!! You can play!!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's Rock&Roll!!")
        print("You're starting off with", points, "points")

        up_or_down = input("Choose.. Up or Down.. ").lower()
        if up_or_down == "up":
            ans = input("Great! There is an Helicopter.. Do you want to jump in? ").lower()

            if ans == "yes":
                print("The helicopter crashed, you're injured and lost 5 points")
                points -= 5
            elif ans == "no":
                print("Good choice! You're safe!")

        elif ans == "down":
            print("Have a sit and someone will come and get you!")

    else:
        print("That's fine", name, "but you're missing big my Friend!")

else:
    print("Sorry", name, "You can't play!")