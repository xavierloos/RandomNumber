import random
myrandom =  random.randint(1,10)
playing = True


while playing:
    guess = int(input("Guess the number: "))
    if guess > myrandom:
        print("LOWER ⮛")
    elif guess < myrandom:
        print("HIGUER ⮙")
    else:
        print("*****************")
        print("*** CORRECT {} ***".format(myrandom))
        print("*****************")
        playing=False