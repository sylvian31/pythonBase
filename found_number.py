import random
import sys

numberMax = 99
numberMin = 1


count_try = 0
nombre_try = 10


def isCorrectNumber(numberMax, numberMin, numberToCheck):
    return numberToCheck >= numberMin and numberToCheck <= numberMax

def isWin(numberToFind, numberChoice):
    return numberToFind == numberChoice

def getPostion(numberChoice, numberToFind):
    if numberChoice < numberToFind:
        print("Too little")
    if numberChoice > numberToFind:
        print("Too big")

def isloose(count_try, nombre_try):
    return count_try == nombre_try

print("Welcome to Found Number !!!")


numberToFind = random.randint(numberMin,numberMax)



print("Enter a number between 0 - 100")

numberChoice = int(input('Enter a number : '))
count_try += 1
while not isWin(numberToFind, numberChoice):
    getPostion(numberChoice, numberToFind)
    numberChoice = int(input('Enter a number : '))
    count_try += 1
    if(isloose(count_try, nombre_try)):
        print("You are a looser !!!")
        break

if(isWin(numberToFind, numberChoice)):
    print("You Win !!!")

def isNumber(number):
    return number.match('^[0-9]+$')


