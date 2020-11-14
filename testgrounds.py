#Open the SAVED.GAM hex file
fileOpen1 = open("SAVED.GAM", encoding = "latin1")

#Open the SAVED.GAM hex file
fileOpen2 = open("SAVED.GAM", "rb+")

f1 = fileOpen1.read()
encodedF = bytearray(f1, "latin1")
stringAgain = encodedF.decode("latin1")
print(stringAgain)
f2 = fileOpen2.read()

print(f1)
# print(f2)
print(f2.decode("latin1"))


fileOpen1.close()
fileOpen2.close()
