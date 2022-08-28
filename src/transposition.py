from pydoc import plain

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
Decrypt the chiper text into plain text by using the rail fence algo
ct - chiper Text
key - number of rails desired

returns - The plain text of the chiper text
"""
def railFenceDe(ct, key):
    newKey = ""
    for i in range(1,key+1):
        newKey = newKey + str(i)
    
    return redFenceDe(ct,newKey)    
        
### RAIL FENCE


### RED FENCE
"""
Encrypts plain text into chiper text by using the red fence algo
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

"""
Decrypt the chiper text into plain text by using the red fence algo
ct - chiper Text
key - the order and number of rails required

returns - The plain text of the chiper text
"""
def redFenceDe(ct, key):
    keyLength = len(key)
    rails = {}
    lengths = {}
    down = True
    curRail = 1

    for i in range(keyLength):
        rails[i+1] = ""
        lengths[i+1] = 0      

    #Get the length of each rail
    for i in range(len(ct)):
        lengths[curRail] = lengths.get(curRail) + 1
        
        if down:
            if curRail == keyLength:
                down = False
                curRail = keyLength-1
            else:
                curRail = curRail + 1
        else:
            if curRail == 1:
                down = True
                curRail = 2
            else:
                curRail = curRail - 1

    curRail = 1
    down = True

    currSeek = 0

    #Get the text for each rail
    for i in range(keyLength):
        rails[int(key[i])] = ct[currSeek: currSeek + lengths.get(int(key[i]))]
        currSeek += lengths.get(int(key[i]))

    plainText = ""
    railPos = [0] * keyLength


    #Dechiper
    for i in range(len(ct)):
        plainText = plainText + rails.get(curRail)[railPos[curRail-1]]

        railPos[curRail-1] += 1

        if down:
            if curRail == keyLength:
                down = False
                curRail = keyLength-1
            else:
                curRail = curRail + 1
        else:
            if curRail == 1:
                down = True
                curRail = 2
            else:
                curRail = curRail - 1

              

    return plainText

### RED FENCE


### FOUR WINDS

def fourWindEn(pt, key):
    if key:
        pass
    mills = [""]*3
    currMill = 0

    for i in range(0, len(pt)):
        if currMill == 0:
            mills[1] = mills[1] + pt[i]
        elif currMill == 1:
            mills[0] = mills[0] + pt[i]    
        elif currMill == 2:
            mills[1] = mills[1] + pt[i]                        
        else:
            mills[2] = mills[2] + pt[i]  
        
        currMill = currMill + 1

        if currMill == 4:
            currMill = 0
    print(mills)
    return ("").join(mills)

### FOUR WINDS
fourWindEn("1234567890", True)
