A=int(input("enter marks:"))
B=int(input("enter marks:"))
C=int(input("enter marks:"))
D=int(input("enter marks:"))
avarage=(A+B+C+D/4)

if avarage >=80 and avarage>=100:
    print("A")
elif avarage >=60 and avarage>=79:
    print("B")
elif avarage>=40 and avarage>=59:
    print("C")
elif avarage>=20 and avarage >=39:
    print("D")
else:
    avarage>=0 and avarage>=19
    print("fail")

