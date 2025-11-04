from random import randint

guess_num = 0
bank = 10
select = ""

while True:
    if select == "Stop" or bank == 0:
        print(f"Bye. Your bank = {bank}")
        break
    answer = randint(1, 50)
    while True:
        guess_num = int(input("Guess the number(1~50): "))
        if bank == 0:
            print("You got no money")
            break
        price = randint(10, 50)
        if guess_num == answer:
            print(f"You're winner! \n You get {price} $")
            bank += price 
            select = input(f"Go | Stop (bank = {bank}): ")
            if select == "Go":
                break
            else:
                break
        elif guess_num < answer:
            bank -= 1
            print(f"Higher! (bank = {bank})")
        else: 
            bank -= 1
            print(f"Lower! (bank = {bank})")