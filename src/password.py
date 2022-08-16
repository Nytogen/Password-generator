import random


alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/"
number = "0123456789"

def createRandString(acceptChar, length):
    output = ""

    for i in range(0,length):
        output = output + acceptChar[random.randint(0, len(acceptChar)-1)]
    return output

def createPassword(acceptChar, passwordLen):
    return createRandString(acceptChar, passwordLen)


def createSalt(acceptChar):
    return createRandString(acceptChar, random.randint(10, 20))
