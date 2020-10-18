p = input("Input p: ")
q = input("Input q: ")
e = input("Input e: ")
M = input("Input M: ")

n = p * q

fen = (p-1) * (q-1)

d = (1 + fen) / e

C = (M ** e) % n
M = (C ** d) % n


print("n " + str(n))
print("fen " + str(fen))
print("d " + str(d))
print("C " + str(C))
print("M " + str(M))