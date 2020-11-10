#Open the SAVED.GAM hex file
fileOpen = open("test.GAM", encoding = "latin1")

#Reads, encode, and store file
f = fileOpen.read()
encodedF = bytearray(f, "latin1") #Holds array of ints

#This function formats hex in little endian
def littleEndianTime(value):
  value = hex(value)
  if (len(value) == 5):
    bit1 = "0" + value[2]
    bit2 = value[3] + value[4]
    return [int(bit2, 16), int(bit1, 16)]
  elif (len(value) == 6):
    bit1 = value[2] + value[3]
    bit2 = value[4] + value[5]
    return [int(bit2, 16), int(bit1, 16)]
  elif (len(value) == 3) or (len(value) == 4):
    return [int(value, 0), 0]
  else:
    print("Not valid")
    return

#User choice menu when changing offsets
userInput = 0
while (userInput != "x"):
  print("Offset Choices")
  print("2. Main Character Stats")
  print("34. Shamino Stats")
  print("66. Iolo Stats")
  print("98. Mariah Stats")
  print("130. Geoffrey Stats")
  print("162. Janna Stats")
  print("194. Julia Stats")
  print("226. Dupre Stats")
  print("258. Katrina Stats")
  print("290. Sentri Stats")
  print("322. Gwenno Stats")
  print("354. Johne Stats")
  print("386. Gorne Stats")
  print("418. Maxwell Stats")
  print("450. Toshi Stats")
  print("482. Saduj Stats")
  print("514. Gold (0-9999)")
  print("516. Food (0-9999)")
  print("518. Keys (0-99)")
  print("519. Gems (0-99)")
  print("520. Torches (0-99)")
  print("522. Margic Carpet (0-99)")
  print("536. Black Badge (0-1)")
  print("576. Magic Axe (0-99)")
  print("682. Sulphurous Ash (0-99)")
  print("683. Ginseng (0-99)")
  print("684. Garlic (0-99)")
  print("685. Spider Silk (0-99)")
  print("687. Black Pearl (0-99)")
  print("693. Party Amount (1-6)")
  print("c. Check Values In Offsets")
  print("x. Exit")
  userInput = input("Type in offset you want to change in game (decimal): ")

  if userInput.isnumeric():    
    userInput = int(userInput)

  #For changing selected character stats
  if (userInput == 2) or (userInput == 34) or (userInput == 66) or (userInput == 98) or (userInput == 130) or (userInput == 162) or (userInput == 194) or (userInput == 226) or (userInput == 258) or (userInput == 290) or (userInput == 322) or (userInput == 354) or (userInput == 386) or (userInput == 418) or (userInput == 450) or (userInput == 382):

    #For offset total
    totalOffSet = userInput

    print("Stat offsets to choose from character: ")
    print("12. Strength (1-100)")
    print("13. Dexterity (1-100)")
    print("14. Intelligence (1-100)")
    print("15. Magic (1-100)")
    print("16. Health (1-999)")
    print("18. Max Health (1-999)")
    print("20. Experience (1-9999)")

    #Add offset using the layout pattern on the file
    addOffSet = input("Type in stat offset you want to change (decimal): ")
    if not addOffSet.isnumeric():
      print("Error on input. Cancel changes")
    else:
      addOffSet = int(addOffSet)
      totalOffSet = totalOffSet + addOffSet #Offset of character stat change

      #For offsets using decimals 1-100
      if (addOffSet == 12) or (addOffSet == 13) or (addOffSet == 14) or (addOffSet == 15):
        setStat = input("Enter amount in stat (1-100): ")

        if setStat.isnumeric():
          setStat = int(setStat)
          if (setStat >= 1) and (setStat <= 100): #Stats changed in offset 12, 13, 14, 15
            print("Character stat set")
            encodedF[totalOffSet] = setStat          
          else:
            print("Invalid stat, cancel changes")
        else:
          print("Error in input, cancel changes")
      
      #For offsets using decimals 1-999
      elif (addOffSet == 16) or (addOffSet == 18):
        setStat = input("Enter amount in stat (1-999): ")

        if setStat.isnumeric():
          setStat = int(setStat)
        
        twoValues = littleEndianTime(setStat)
        encodedF[totalOffSet] = twoValues[0]
        encodedF[totalOffSet + 1] = twoValues[1]
        print("Character stat set")

      #For offsets using decimals 1-9999
      elif (addOffSet == 20):
        setStat = input("Enter amount in stat (1-9999): ")

        if setStat.isnumeric():
          setStat = int(setStat)
        
        twoValues = littleEndianTime(setStat)
        encodedF[totalOffSet] = twoValues[0]
        encodedF[totalOffSet + 1] = twoValues[1]
        print("Character stat set")

      else:
        print("Invalid stat offset, cancel changes")
  
  #Change item numbers involving numbers 0-99
  elif (userInput == 518) or (userInput == 519) or (userInput == 520) or (userInput == 522) or (userInput == 576) or (userInput == 682) or (userInput == 683) or (userInput == 684) or (userInput == 685) or (userInput == 518):
    setAmount = input("Set amount of items (0-99): ")
    if setAmount.isnumeric():
      setAmount = int(setAmount)
      print("Item Amount Changed")
    else:
      print("Error in input, cancel changes")

    if (setAmount >= 0) and (setAmount <= 99):
      encodedF[userInput] = setAmount
      print("Item amount changed")
    else:
      print("Number out of range, cancel changes")
  
  #Change item number involving numbers 0-9999
  elif (userInput == 514) or (userInput == 516):
    setAmount = input("Set amount of items (0-9999): ")
    if setAmount.isnumeric():
      setAmount = int(setAmount) # Still working on this
      twoValues = littleEndianTime(setStat)
      encodedF[totalOffSet] = twoValues[0]
      encodedF[totalOffSet + 1] = twoValues[1]
      print("Item Amount Changed")
    else:
      print("Error in input, cancel changes")
  
  #One choice item (black badge)
  elif (userInput == 687):
    setAmount = ("Enter amount of the item (0-1):")
    if setAmount.isnumeric():
      if (setAmount == 0):
        encodedF[userInput] = 0
        print("Item Amount Changed")
      elif (setAmount == 1):
        encodedF[userInput] = 255
        print("Item Amount Changed")
      else:
        print("Input error, cancel changes")
    else:
      print("Error in input, cancel changes")

  #Check all values in offsets
  elif (userInput != "c"):
    for i in range(len(encodedF)):
      print(str(i) + ". " + str(encodedF[i]))

  elif (userInput != "x"): #For any offset not listed
    print("Invalid choice")

fileOpen.close

#Write file in byte form
newFile = open("test.GAM", "wb+")

newFile.write(encodedF)

newFile.close()
