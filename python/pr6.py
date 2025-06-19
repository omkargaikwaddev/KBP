def count(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
    print("Upper case characters in string are:",upper)
    print("lower case characters in string are:",lower)


count("Omkar Gaikwad")