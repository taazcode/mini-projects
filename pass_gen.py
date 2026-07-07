import random
import string

while True:
    length=int(input("Enter the length of the password:"))
    upper =input("Use of uppercase:(y/n)?")
    lower=input("Use of lower:(y/n)?")
    number =input("Use of number:(y/n)?")
    Symbol =input("Use of symbols:(y/n)?")

    if upper =="y":
        def gen_random_upper():
         char_U = string.ascii_uppercase
         Uran = [random.choice(char_U) for i in range (1,16)]
         return Uran
    chau=gen_random_upper()
    datau="".join(random.choice(chau)for i in range(8))
    

    if lower =="y" :
        def gen_random_lower():
        
         char_L= string.ascii_lowercase
         Lran = [random.choice(char_L) for i in range (1,16)]
         return Lran
    chaL=gen_random_lower()
    dataL="".join(random.choice(chaL)for i in range(8))
    
    if number == "y" or "yes":
     def gen_rand_num():
        char_N = string.digits
        nran = [random.choice(char_N) for i in range (1,16)]
        return nran
    chaN=gen_rand_num()
    dataN="".join(random.choice(chaN)for i in range(16))

    if Symbol == "y" or "yes":
        def rand_sym():
         char_S = string.punctuation
         Sran = [random.choice(char_S) for i in range (1,16)]
         return Sran
    chaS=rand_sym()
    dataS="".join(random.choice(chaS)for i in range(16))
    # passwhole string
    password =datau+dataL+dataS+dataN
    # password generator
    def pass_gen(password=password,length=length):
       
        final_pass="".join(random.choice(password)for _ in range(length))
        return final_pass
    fi_pass=pass_gen()
    print(fi_pass)
    score = 0
    def fuck(upper, lower, Symbol, number,length):

        global score 
 
        if upper == "y" or upper == "yes":
            score += 1
        if length >= 12:
            score += 1
        if lower == "y" or lower == "yes":
            score += 1
        if number == "y" or number == "yes":
            score += 1
        if Symbol == "y" or Symbol == "yes":
            score += 1

        if score >= 4:
            strength = "strong"
        elif score == 3:
            strength = "medium"
        else:
            strength = "weak"
        return strength , score
    score ,strength =fuck(upper,lower,number,Symbol,length)
    print("Strength:",score ,"Score:",strength)
    stay=str(input("want another?(y/n):"))
    if stay =="n":
       break

 
