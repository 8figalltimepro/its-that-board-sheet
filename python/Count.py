def count():
    f=open("Mytext.txt","r")
    content = f.read()
    v=0
    cons=0
    upperch=0
    lowerch=0
    for ch in content:
        if ch.islower():
            lowerch+=1
        elif ch.isupper():
            upperch+=1
        ch=ch.lower()
        if ch in 'aeiou':
            v+=1
        elif ch in 'bcdfghjklmnpqrstvwxyz':
            cons+=1
    f.close()
    print("Vowels are : ",v)
    print("consonants are : ",cons)
    print("Lower case letters are : ",lowerch)
    print("Upper case letters are : ",upperch)

count()
