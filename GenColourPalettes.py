import tkinter as tk
import time as time
EcolourName = []
EcolourCode = []
LcolourName = []
LcolourCode = []
EfileName = []


def createFile(fileName, names, codes):
    if not(fileName == ""):
        cssFile = open(fileName + ".css", "w+")
    else:
        cssFile = open("Sample Colour Palette"+str(time.ctime())+".css", "w+")
    cssCode = ""
    for i in range(len(names)):
        cssCode += ".bg-"+names[i] + \
            "{\n\tbackground-color: #"+codes[i] + ";\n}\n"
    for i in range(len(names)):
        cssCode += ".border-"+names[i] + \
            "{\n\tborder-color: #"+codes[i] + ";\n}\n"
    cssFile.write(cssCode)
    cssFile.flush()
    cssFile.close()


def getColNamesCodes():
    colourNames = []
    colourCodes = []
    for name in EcolourName:
        colourNames.append(name.get())
    for code in EcolourCode:
        colourCodes.append(code.get())
    fileName = EfileName[0].get()
    createFile(fileName, colourNames, colourCodes)
    return


def setcolourEntries():
    numColours = int(EnumColours.get())
    if(numColours < 100):
        createColourEntries(numColours)


def createColourEntries(numColours):
    numIndicator = ""
    rowNum = 3
    for i in range(1, numColours+1):
        if(i == 1):
            numIndicator = "first"
        elif(i == 2):
            numIndicator = "second"
        elif(i == 3):
            numIndicator = "third"
        elif(i == 11 or i % 10 == 0):
            numIndicator = str(i) + "th"
        elif (i % 10 == 1):
            numIndicator = str(i) + "st"
        elif(i % 10 == 2):
            numIndicator = str(i) + "nd"
        elif(i % 10 == 3):
            numIndicator = str(i) + "rd"
        else:
            numIndicator = str(i) + "th"
        LcolourName.append(tk.Label(text="Enter your "+numIndicator+" colour"))
        LcolourCode.append(tk.Label(text="Enter the hex code for your "+numIndicator+" colour"))
        EcolourName.append(tk.Entry(window))
        EcolourCode.append(tk.Entry(window))

    for i in range(len(LcolourName)):
        LcolourName[i].grid(row=rowNum, column=0, sticky=tk.E + tk.W)
        LcolourCode[i].grid(row=rowNum, column=2, sticky=tk.E + tk.W)
        rowNum += 1

    rowNum = 3
    for name in EcolourName:
        name.grid(row=rowNum, column=1, sticky = tk.E + tk.W)
        rowNum += 1
    
    rowNum = 3
    for code in EcolourCode:
        code.grid(row=rowNum, column=5, sticky = tk.E+tk.W)
        rowNum += 1
    LfileName = tk.Label(window, text="Enter the filename")
    EfileName.append(tk.Entry(window))
    LfileName.grid(row=rowNum, column=0)
    EfileName[0].grid(row=rowNum, column=1)
    BcreatePalette = tk.Button(
        window, text="Create Palette", command=getColNamesCodes)
    BcreatePalette.grid(row=5, column=6)


window = tk.Tk()
window.title("Generate Colour Palettes")
LnumColours = tk.Label(window, text="Enter the number of colours you want in your palette", font=(
    "Ubuntu", 12), padx=3, pady=3)
LnumColours.grid(column=0, row=0, columnspan=3)
EnumColours = tk.Entry(window, text="Colour", width=20, font=('Ubuntu', 12))
EnumColours.grid(column=0, row=1)
bt = tk.Button(window, text="Enter", bg="black",
               fg="white", command=setcolourEntries)
bt.grid(column=0, row=2)
window.mainloop()
