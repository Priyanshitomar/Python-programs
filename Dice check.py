import random
while True:
    dice = random.randint(1, 6)
    print("Dice rolled:", dice)
    if dice == 6:
        print("Yatzy!")
        break
