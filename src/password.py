import random


alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/"
number = "0123456789"

def createRandString(acceptChar, length):
    output = ""

    for i in range(0,length):
        output = output + acceptChar[random.randint(0, len(acceptChar)-1)]
    return output

def createPassword(passwordLen, saltLen):
    password = createRandString(alpha+symbol+number, passwordLen)
    salt = createRandString(alpha+symbol+number, saltLen)

    print(password)
    print(salt)

for i in range(20):
    createPassword(24,10)
    print("---------------")