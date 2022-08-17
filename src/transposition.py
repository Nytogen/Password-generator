### RAIL FENCE
def railFenceEn(pt, key, asList):
    rails = [""] * key
    down = True
    curRail = 0

    for i in range(0, len(pt)):
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
        

def railFenceDe(ct, key):
    return None

### RAIL FENCE
