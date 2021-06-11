import random


def guess_num(count=1, numb=random.randint(0, 100)):
    ans = int(input("Enter the number between 0 and 100\n: "))
    if ans == numb:
        print("You guessed!")
    elif count == 10:
        print(f"You did not guess. The num is {numb}")
    else:
        if ans > numb:
            print("The hidden number is less")
            count += 1
        else:
            print("The hidden number is greater")
            count += 1
        guess_num(count)


guess_num()
