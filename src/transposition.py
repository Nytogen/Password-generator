### RAIL FENCE
"""
Encrypts plain text into chiper text by using the rail fence algo
pt - Plain text
key - number of rails desired
asList- Return the chiper text as a list of rails if true, otherwise as a string

returns - A list of rails or a string of the chiper text
"""
def railFenceEn(pt, key, asList):
    newKey = ""
    for i in range(1,key+1):
        newKey = newKey + str(i)
    
    return redFenceEn(pt,newKey,asList)

"""
Encrypts the chiper text into plain text by using the rail fence algo
ct - chiper Text
key - number of rails desired

returns - The plain text of the chiper text
"""
def railFenceDe(ct, key):
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

    return plainText
        
### RAIL FENCE


### RED FENCE
"""
Encrypts plain text into chiper text by using the rail fence algo
pt - Plain text
key - number of rails desired and the order desired
asList- Return the chiper text as a list of rails if true, otherwise as a string

returns - A list of rails or a string of the chiper text
"""
def redFenceEn(pt, key, asList):
    keyLength = len(key)
    rails = [""] * keyLength
    down = True
    curRail = 0

    for i in range(len(pt)):
        rails[curRail] += pt[i]        

        if down:
            curRail = curRail + 1
            if curRail >= keyLength:
                down = False
                curRail = keyLength - 2
        else:
            curRail = curRail - 1
            if curRail < 0:
                down = True
                curRail = 1

        newOrder = [""]*keyLength
        for i in range(keyLength):
            newOrder[i] = rails[int(key[i])-1]

    if asList:
        return newOrder
    return ''.join(newOrder)

### RED FENCE