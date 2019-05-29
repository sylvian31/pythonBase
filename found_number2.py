import random
import sys

numberMax = 99
numberMin = 1

nombreTour = 10

numberToFind = random.randint(numberMin,numberMax)


def isWin(numberToFind, numberChoice):
    return numberToFind == numberChoice

def getPostion(numberChoice, numberToFind):
    if numberToFind == numberChoice:
        print("Win !!!!")
        return True
    elif numberChoice < numberToFind:
        print("Too little")
        return False
    else:
        print("Too big")
        return False


print("Welcome to Found Number !!!")


print("Enter a number between 0 - 100")


for i in range(nombreTour):
    numberChoice = int(input('Enter a number : '))
    if getPostion(numberChoice, numberToFind):
        break
    if i == nombreTour - 1 :
        print("losser !!!")
        break




