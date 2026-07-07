import string 

Check=input("Enter")

charU=string.ascii_uppercase
score = 0

def upper_check(score=score):
    
    for i in Check:
        if i in charU:
            upper="y"
            score += 1
            break
        else:
            upper= "n"
    return upper
u=upper_check()
print(u)

charL=string.ascii_lowercase

def lower_check(score=score):
    
    for i in Check:
        if i in charL:
            lower="y"
            score += 1
            break
        else:
            lower= "n"
    return lower
l=lower_check()
print(l)

Charnum=string.digits

def number_check(score=score):
    
    for i in Check:
        if i in Charnum:
            num="y"
            score += 1
            break
        else:
            num= "n"
    return num
d=number_check()
print(d)

CharS=string.punctuation

def symbol_check(score=score):
    
    for i in Check:
        if i in CharS:
            symbol="y"
            score += 1
            break
        else:
            symbol= "n"
    return symbol
p=symbol_check()
print(p)
if score ==5:
    print("Your password is strong")
if score==4:
    print("Your password is good")
if score ==3:
    print("Your password is medium")
if score ==2 or score ==1:
    print("Your password is weak")