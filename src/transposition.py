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
"""
Encrypt the plain text into chiper text by using the Four Windsalgo

example of four Winds
input - 1234 going clockwise
  2
1   3
  4
output - 2134

pt - plain Text
key - clockwise or counter clockwise

returns - The chiper text
"""
def fourWindEn(pt, key):
    if key:
        top = 0
        bottom = 2
    else:
        top = 2
        bottom = 0
    mills = [""]*3
    currMill = 0

    for i in range(0, len(pt)):
        if currMill == 0:
            mills[1] = mills[1] + pt[i]
        elif currMill == 1:
            mills[top] = mills[top] + pt[i]    
        elif currMill == 2:
            mills[1] = mills[1] + pt[i]                        
        else:
            mills[bottom] = mills[bottom] + pt[i]  
        
        currMill = currMill + 1

        if currMill == 4:
            currMill = 0
    return ("").join(mills)

"""
Decrypt the chiper text into plain text by using the Four Windsalgo

example of four Winds

ct - chiper Text
key - clockwise or counter clockwise

returns - The plain text of the chiper text
"""
def fourWindDe(ct, key):
    mills = [""]*3
    millsPos = [0]*3
    currMill = 0
    numMills = len(ct)//4
    leftMills = len(ct)%4
    pt = ""

    fourWindSetMillsClock(ct, mills, numMills, leftMills)
    
    if key:
        top = 0
        bottom = 2
        fourWindSetMillsClock(ct, mills, numMills, leftMills)
    else:
        top = 2
        bottom = 0
        fourWindSetMillsCounter(ct, mills, numMills, leftMills)

    for i in range(len(ct)):
        if currMill == 0:
            pt = pt + mills[1][millsPos[1]]
            millsPos[1] = millsPos[1] + 1
        elif currMill == 1:
            pt = pt + mills[top][millsPos[top]]
            millsPos[top] = millsPos[top] + 1
        elif currMill == 2:
            pt = pt + mills[1][millsPos[1]]
            millsPos[1] = millsPos[1] + 1              
        else:
            pt = pt + mills[bottom][millsPos[bottom]]
            millsPos[bottom] = millsPos[bottom] + 1

        currMill = currMill + 1

        if currMill == 4:
            currMill = 0      

    return pt

def fourWindSetMillsClock(ct, mills, numMills, leftMills):
    if leftMills == 3:
        mills[0] = ct[0: numMills + 1]
        mills[1] = ct[numMills + 1: (3 * numMills)+3]
        mills[2] = ct[(3*numMills) + 3:]
    elif leftMills == 2:
        mills[0] = ct[0: numMills + 1]
        mills[1] = ct[numMills + 1: (3 * numMills)+2]
        mills[2] = ct[(3*numMills) + 2:]
    elif leftMills == 1:
        mills[0] = ct[0: numMills]
        mills[1] = ct[numMills: (3 * numMills)+1]
        mills[2] = ct[(3*numMills) + 1:]
    else:
        mills[0] = ct[0: numMills]
        mills[1] = ct[numMills: (3 * numMills)]
        mills[2] = ct[3*numMills:]

def fourWindSetMillsCounter(ct, mills, numMills, leftMills):
    if leftMills == 3:
        mills[0] = ct[0: numMills + 1]
        mills[1] = ct[numMills + 1: (3 * numMills)+2]
        mills[2] = ct[(3*numMills) + 2:]
    elif leftMills % 4 != 0:
        mills[0] = ct[0: numMills]
        mills[1] = ct[numMills: (3 * numMills)+1]
        mills[2] = ct[(3*numMills) + 1:]
    else:
        mills[0] = ct[0: numMills]
        mills[1] = ct[numMills: (3 * numMills)]
        mills[2] = ct[3*numMills:]    

### FOUR WINDS

### COMPLETE COLUMNAR

def completeColumnarEn(pt, key):
    columns = [""]*len(key)

    for i in range(len(pt)):
        columns[i%len(columns)] = columns[i%len(columns)]  + pt[i]

    ct = ""
    keyColumns = {}
    pos = 0

    for i in key:
        keyColumns[int(i)-1] = pos
        pos = pos + 1    

    for i in range(len(key)):
        ct = ct + columns[keyColumns.get(i)]
    
    return ct

def completeColumnarDe(ct, key):
    keyLength = len(key)
    columns = [0]*keyLength
    columnText = [""]*keyLength
    seek = 0

    columnLength = len(ct) // keyLength
    remaining = len(ct) % keyLength

    for i in range(keyLength):
        if i < remaining:
            columns[int(key[i])-1] = columnLength + 1
        else:
            columns[int(key[i])-1] = columnLength

    for i in range(keyLength):
        columnText[i] = ct[seek:seek + columns[i]]
        seek = seek + columns[i]        

    columnsPos = [0]*keyLength
    pt = ""

    for i in range(len(ct)):
        nextCol = int(key[i%keyLength]) - 1
        pt = pt + columnText[nextCol][columnsPos[i%keyLength]]
        columnsPos[i%keyLength] = columnsPos[i%keyLength] + 1

    return pt

### COMPLETE COLUMNAR

print(completeColumnarDe("25314", "312"))

