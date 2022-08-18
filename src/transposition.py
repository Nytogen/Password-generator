### RAIL FENCE
"""
Encrypts plain text into chiper text by using the rail fence algo
pt - Plain text
key - number of rails desired
asList- Return the chiper text as a list of rails if true, otherwise as a string

returns - A list of rails or a string of the chiper text
"""
def railFenceEn(pt, key, asList):
    rails = [""] * key
    down = True
    curRail = 0

    for i in range(len(pt)):
        rails[curRail] += pt[i]        

        if down:
            curRail = curRail + 1
            if curRail >= key:
                down = False
                curRail = key - 2
        else:
            curRail = curRail - 1
            if curRail < 0:
                down = True
                curRail = 1

    if asList:
        return rails
    return ''.join(rails)

"""
Encrypts the chiper text into plain text by using the rail fence algo
ct - chiper Text
key - number of rails desired

returns - The plain text of the chiper text
"""
def railFenceDe(ct, key, asList):
    rails = [""] * key
    lengths = [0]*key
    down = True
    curRail = 0

    #Get the length of each rail
    for i in range(len(ct)):
        lengths[curRail] = lengths[curRail] + 1

        if down:
            curRail = curRail + 1
            if curRail >= key:
                down = False
                curRail = key - 2
        else:
            curRail = curRail - 1
            if curRail < 0:
                down = True
                curRail = 1
    
    curRail = 0
    down = True

    currSeek = 0

    #Get the text for each rail
    for i in range(key):
        rails[i] = ct[currSeek: currSeek+lengths[i]]
        currSeek += lengths[i]

    plainText = ""
    railPos = [0] * key

    #Dechiper
    for i in range(len(ct)):
        plainText = plainText + rails[curRail][railPos[curRail]]

        railPos[curRail] += 1

        if down:
            curRail = curRail + 1
            if curRail >= key:
                down = False
                curRail = key - 2
        else:
            curRail = curRail - 1
            if curRail < 0:
                down = True
                curRail = 1       

    print(plainText)
    return None
        
### RAIL FENCE