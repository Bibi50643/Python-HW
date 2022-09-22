import random
number=random.randrange(0,100)
print(number)
def guess():
    result= False
    while result ==False:
        you= int(input("Guess:"))
        if number==you:
            result= True
            print("BINGO!")
            return True
        elif you<number:
            print('The number is more')
        elif you>number:
            print('The number is fewer')
guess()