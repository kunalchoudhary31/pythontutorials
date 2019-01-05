print("""You Enter dark room with 2 doors.
Do you go through door #1 or door #2""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a chesse cake.")
    print("What do you do?")
    print("1. Take the care.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else:
        print(f"Well doing {bear} was better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("You fucked up!")
        print("Good job!")
    else:
        print("You again fucked up")
        print("Good job!")

else:
    print("Good night!")
