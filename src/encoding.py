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