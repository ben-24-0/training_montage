passw=input("Enter Password:")
cap,low,alpha,special,num = False,False,False,False,False
if (len(passw)<8):
    print("Password Must atleast be 8 Characters")
else:
    for i in passw:
        if i.isalpha():
            alpha=True
            if i.islower():
                low=True
            else:
                cap=True
        elif i.isdigit():
            num=True
        elif ord(i)!=32:
            special=True

    if not alpha:
        print("Password Must Contain an Alphabet")
    if not low:
        print("Password Must Contain a Lower Case Letter")
    if not cap:
        print("Password Must Contain an Upper Case Letter")
    if not num:
        print("Password Must Contain a Number")
    if not special:
        print("Password Must Contain a Special Character")

    if cap and alpha and low and special and num:
        print("Password Valid")
