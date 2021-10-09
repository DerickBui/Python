import tkinter as tk # Import tkinter GUI library
import random as rand
import serial # Import serial library for python connect with arduino (do pip install pyserial on consolepip)
import can # Import CAN library (do python pip install python-can)

# Root for application------------------------------------------------------------------------------------
root = tk.Tk()

# Functions-----------------------------------------------------------------------------------------------
# def randomNumber(): # for test, will be trashed
#     global upperPropSystemLabels
#     upperPropSystemLabels[2]["text"] = "Temp: " + str(rand.randint(0,100))
#     upperPropSystemLabels[2].after(1, randomNumber)

# Create size for GUI window------------------------------------------------------------------------------
# Window size presets
HEIGHT = 1080 
WIDTH = 1920

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

#Group 1 Mode Display-------------------------------------------------------------------------------------
#Create group 1 frame
group1ModeFrame = tk.Frame(root, bg="Aqua", bd=5)
group1ModeFrame.place(relx=0, rely=0, relwidth=2/3, relheight=1)

# Create top label frame and three smaller frames for nodes-----------------------------
topLabelFrame = tk.Frame(group1ModeFrame, bg="black", bd=5)
topLabelFrame.place(relx=0.5, rely=0, relwidth=0.9, relheight=0.2, anchor="n")

# Number of nodes needed
nodes = 3

# nodeFrames[0]: Prop System Node Frame
# nodeFrames[1]: Engine Node Frame
# nodeFrames[2]: Pad Group Node Frame
nodeFrames = [0] * nodes
for i in range(nodes):
    nodeFrames[i] = tk.Frame(topLabelFrame, bg="white", bd=5)
    nodeFrames[i].place(relx=((1/nodes) + 0.005)*i, rely=0, relwidth=(1/(nodes + 0.1)), relheight=1)


# Upper Prop System node labels------------------------------------
# upperPropSystemLabels[0]: Node Name (Upper Prop System Node)
# upperPropSystemLabels[1]: Upper Prop System Activity
# upperPropSystemLabels[2]: Uppoer Prop System Temperature
# upperPropSystemLabels[3]: Sampling / Bus Info
upperPropSystemLabels = [0] * 4
for i in range(4):
    upperPropSystemLabels[i] = tk.Label(nodeFrames[0], text="", bg="blue", anchor="w")
    upperPropSystemLabels[i].place(relx=0, rely=(1/4)*i, relwidth=2/3, relheight=1/4)

upperPropSystemLabels[0]["text"] = "Upper Prop System Node"
upperPropSystemLabels[1]["text"] = "Activity: "
upperPropSystemLabels[2]["text"] = "Temp: "
upperPropSystemLabels[3]["text"] = "Sampling / Bus Info"

# Engine node labels------------------------------------
# engineLabels[0]: Node Name (Engine Node)
# engineLabels[1]: Engine Activity
# engineLabels[2]: Engine Temperature
# engineLabels[3]: Sampling / Bus Info
engineLabels = [0] * 4
for i in range(4):
    engineLabels[i] = tk.Label(nodeFrames[1], text="", bg="blue", anchor="w")
    engineLabels[i].place(relx=0, rely=(1/4)*i, relwidth=2/3, relheight=1/4)

engineLabels[0]["text"] = "Upper Prop System Node"
engineLabels[1]["text"] = "Activity: "
engineLabels[2]["text"] = "Temp: "
engineLabels[3]["text"] = "Sampling / Bus Info"

# Pad Ground node labels------------------------------------
# padGroundLabels[0]: Node Name (Pad Ground Node)
# padGroundLabels[1]: Pad Ground Activity
# padGroundLabels[2]: Pad Ground Temperature
# padGroundLabels[3]: Sampling / Bus Info
padGroundLabels = [0] * 4
for i in range(4):
    padGroundLabels[i] = tk.Label(nodeFrames[2], text="", bg="blue", anchor="w")
    padGroundLabels[i].place(relx=0, rely=(1/4)*i, relwidth=2/3, relheight=1/4)

padGroundLabels[0]["text"] = "Pad Ground Node"
padGroundLabels[1]["text"] = "Activity: "
padGroundLabels[2]["text"] = "Temp: "
padGroundLabels[3]["text"] = "Sampling / Bus Info"

# nodeFrameStateLabels[0]: Prop System Node State Label
# nodeFrameStateLabels[1]: Engine Node State Label
# nodeFrameStateLabels[2]: Pad Group Node State Label
nodeFrameStateLabels = [0] * nodes
for i in range(nodes):
    nodeFrameStateLabels[i] = tk.Label(nodeFrames[i], text="", bg="aqua")
    nodeFrameStateLabels[i].place(relx=2/3, rely=2/3, relwidth=(1/3), relheight=1/3)

# Create 12 Button Frame---------------------------------------
g1RowFrame1 = tk.Frame(group1ModeFrame, bg="Red", bd=5)
g1RowFrame1.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.2, anchor="n")

# List to store buttons for g1RowFrame1
g1ButtonRowList1 = [0]*12

# Create first row of buttons
for i in range(12): # Create buttons for g1ForFrame1
    if (i < 6):
        g1ButtonRowList1[i] = tk.Button(g1RowFrame1, text="G1 F1 Button " + str(i + 1))
        g1ButtonRowList1[i].place(relx=((1/6) * i), rely=0, relwidth=(1/6), relheight=0.5)
    else:
        g1ButtonRowList1[i] = tk.Button(g1RowFrame1, text="G1 F1 Button " + str(i + 1))
        g1ButtonRowList1[i].place(relx=((1/6) * (i - 6)), rely=0.5, relwidth=(1/6), relheight=0.5)


# Create 6 Button Frame
g1RowFrame2 = tk.Frame(group1ModeFrame, bg="Red", bd=5)
g1RowFrame2.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.1, anchor="n")

# List to store buttons for g1RowFrame2
g1ButtonRowList2 = [0]*6

# Create row of buttons
for i in range(6): # Create buttons for g1ForFrame1
    g1ButtonRowList2[i] = tk.Button(g1RowFrame2, text="G1 F2 Button " + str(i + 1))
    g1ButtonRowList2[i].place(relx=((1/6) * i), rely=0, relwidth=(1/6), relheight=1)

#Group 2 Mode Display--------------------------------------------------------------------------------------
#Create group 2 frame
group2ModeFrame = tk.Frame(root, bg="Blue", bd=5)
group2ModeFrame.place(relx=2/3, rely=0, relwidth=1/3, relheight=1)

# Realtime stuff
# root.after(1, randomNumber)

# Start window--------------------------------------------------------------------------------------------
root.mainloop()
