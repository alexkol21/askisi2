def ROT13(str):
    y = 0
    x = 0
    endpos1 = 0
    endpos2 = 0
    str1 = ''
    upcaseletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowecaseletters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in str:
        checkcase = i.isupper()
        if checkcase == False:
            while i != lowecaseletters[y]:
                y += 1
            if y > 12:
                endpos1 = y + 13 - 25 - 1
            else:
                endpos1 = y + 13
            str1 += lowecaseletters[endpos1]
        else:
            while i != upcaseletters[x]:
                x += 1
            if x > 12:
                endpos2 = x + 13 - 25 - 1
            else:
                endpos2 = x + 13
            str1 += upcaseletters[endpos2]
    return str1



str1 = input("Δωσε μια σειρα γραμματων.: ")
print(ROT13(str1))