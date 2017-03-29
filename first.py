print " We are now going to implement some fiunctions "


def Complement(inBitStr="0"):
    outBitStr = ""
    for bit in inBitStr:
        if bit == "0":
            outBitStr += "1"
        else:
            outBitStr += "0"
    return outBitStr


print Complement("1010101111")


def Qencoder(value=0.0, inBits=4, fracbits=2, signed=1, roundMethod="ROUND"):
    if roundMethod == "ROUND":
        roundok = True
    if roundMethod == "CEIL":
        roundok = True
    if roundMethod == "FLOOR":
        roundok = True
    if roundok == False:
        raise ValueError("Error: Value of roundmethod should be either of ROUND CEIL FLOOR")
        return "error roundmethod"

    if signed == 1:
        isSigned = True
    else:
        isSigned = False

 abs()