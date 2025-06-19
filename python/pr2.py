s1 = int(input("Enter marks of sub1:"))
s2 = int(input("Enter marks of sub2:"))
s3 = int(input("Enter marks of sub3:"))
s4 = int(input("Enter marks of sub4:"))
s5 = int(input("Enter marks of sub5:"))

avg = (s1 + s2 + s3 + s4 + s5 )/ 5
if avg>85 and avg<100:
    print("A Grade")
elif avg>75 and avg<85:
    print("B Grade")
elif avg>65 and avg<75:
    print("C Grade")
elif avg>55 and avg<65:
    print("D Grade")
else:
    print("Better Luck next time")
