# Import tkinter library, only reason to import it
# like this is just to mark down tk methods
import tkinter as tk

# All button methods------------------------------------------------------------------------------------
def ActivateButton(number):
    global buttonStringList
    if (buttonStringList[number].get() == "Off"):
        buttonStringList[number].set("On")
        blankFunction(number)
    else:
        buttonStringList[number].set("Off")
        blankFunction(number)

def DeactivateButton(number):
    pass

def blankFunction(number):
    pass

def SwitchMode(number): # Function that switch mode
    global fireModeOn
    global keyNum
    global stringMode
    if (number == 0): # Turns on Test Mode
        fireModeOn = False
        keyNum = 0 # Reset key num
        stringMode.set("Test Mode")
        print("Test Mode On")
    elif (number == 1): # Turns on Fire Mode
        if (keyNum < 2): # Number Key increments
            keyNum += 1
            stringMode.set("Press " + str(3 - keyNum) + " more times to turn on Fire Mode")
            print("Key incremented")
        elif (keyNum == 2): # Fire mode turns on after number key is pressed three times
            fireModeOn = True
            stringMode.set("Fire Mode")
            print("Fire Mode On")
    check()

def check():
    print(fireModeOn)

# Root for application------------------------------------------------------------------------------------
root = tk.Tk()

# Create size for GUI window------------------------------------------------------------------------------
# Window size presets
HEIGHT = 1080 
WIDTH = 1920

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Frame to have all control buttons-----------------------------------------------------------------------
buttonFrame = tk.Frame(root, bg="Blue")
buttonFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

# Buttons
button1 = tk.Button(buttonFrame, text="Button 1", command=lambda: ActivateButton(0))
button1.place(relx=0, rely=0, relwidth=0.1, relheight=0.166)
button2 = tk.Button(buttonFrame, text="Button 2", command=lambda: ActivateButton(1))
button2.place(relx=0, rely=0.1666, relwidth=0.1, relheight=0.166)
button3 = tk.Button(buttonFrame, text="Button 3", command=lambda: ActivateButton(2))
button3.place(relx=0, rely=0.3332, relwidth=0.1, relheight=0.166)
button4 = tk.Button(buttonFrame, text="Button 4", command=lambda: ActivateButton(3))
button4.place(relx=0, rely=0.4998, relwidth=0.1, relheight=0.166)
button5 = tk.Button(buttonFrame, text="Button 5", command=lambda: ActivateButton(4))
button5.place(relx=0, rely=0.6664, relwidth=0.1, relheight=0.166)
button6 = tk.Button(buttonFrame, text="Button 6", command=lambda: ActivateButton(5))
button6.place(relx=0, rely=0.8330, relwidth=0.1, relheight=0.166)

# Button String Variables
buttonStringList = [0] * 6

for i in range(len(buttonStringList)):
    buttonStringList[i] = tk.StringVar()
    buttonStringList[i].set("Off")

buttonLabel1 = tk.Label(buttonFrame, textvariable=buttonStringList[0], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel1.place(relx=0.1, rely=0, relwidth=0.1, relheight=0.166)
buttonLabel2 = tk.Label(buttonFrame, textvariable=buttonStringList[1], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel2.place(relx=0.1, rely=0.1666, relwidth=0.1, relheight=0.166)
buttonLabel3 = tk.Label(buttonFrame, textvariable=buttonStringList[2], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel3.place(relx=0.1, rely=0.3332, relwidth=0.1, relheight=0.166)
buttonLabel4 = tk.Label(buttonFrame, textvariable=buttonStringList[3], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel4.place(relx=0.1, rely=0.4998, relwidth=0.1, relheight=0.166)
buttonLabel5 = tk.Label(buttonFrame, textvariable=buttonStringList[4], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel5.place(relx=0.1, rely=0.6664, relwidth=0.1, relheight=0.166)
buttonLabel6 = tk.Label(buttonFrame, textvariable=buttonStringList[5], bg="white", borderwidth=2, relief="solid", anchor="center")
buttonLabel6.place(relx=0.1, rely=0.8330, relwidth=0.1, relheight=0.166)


# Frame to contain the current mode shown on GUI-----------------------------------------------------------
# Mode safety variables
fireModeOn = False # Boolean for mode (False means Test Mode / True means Fire Mode)
keyNum = 0 # Number of times fire mode button pressed will activate fire mode
stringMode = tk.StringVar() # String for display current mode
stringMode.set("Test Mode") # Set string

modeDisplayFrame = tk.Frame(root, bg="green", bd = 5)
modeDisplayFrame.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.05)

modeLabel = tk.Label(modeDisplayFrame, textvariable=stringMode, bg="white", borderwidth=2, relief="solid", anchor="center")
modeLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Frame to contain test and actual fire button-------------------------------------------------------------
testFrame = tk.Frame(root, bg="green", bd=5)
testFrame.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

testModeButton = tk.Button(testFrame, text="Test Mode", command=lambda: SwitchMode(0))
testModeButton.place(relx=0, rely=0, relwidth=0.5, relheight=1)

fireModeButton = tk.Button(testFrame, text="Fire Mode", command=lambda: SwitchMode(1))
fireModeButton.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

# To type in input
# entry = tk.Entry(frame, bg="white")
# entry.pack()

# Initialize settings
SwitchMode(0)

# Start window
root.mainloop()
