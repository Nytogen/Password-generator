def ceaserShiftEn(pt, key):
    ct = ""

    for i in pt:
        ct = ct + chr(ord(i)+key)
    
    return ct

def ceaserShiftDe(ct, key):
    pt = ""

    for i in ct:
        pt = pt + chr(ord(i)-key)
    
    return pt

def rot13En(pt):
    return ceaserShiftEn(pt, 13)

def rot13De(ct):
    return ceaserShiftDe(ct, 13)


def atbashEn(pt):
    ct = ""

    for i in pt:
        if i.isalpha():
            if i.isupper():
                shift = ord(i) - 65
                ct = ct + chr(90 - shift)
            else:
                shift = ord(i) - 97
                ct = ct + chr(122 - shift)
        else:
            ct = ct + i
    
    return ct