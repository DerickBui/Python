q = input("Enter prime number for q: ")
p1 = input("Enter prime number for p1: ")
p2 = input("Enter prime number for p2: ")
e = input("Enter smaller prime number for e: ")

ya = e**p1
yb = e**p2

ya = ya % q
yb = yb % q

ka = yb**p1
kb = ya**p2
ka = ka % q
kb = kb % q

print(ya)
print(yb)
print(ka)
print(kb)