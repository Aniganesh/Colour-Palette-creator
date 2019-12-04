def getNumColours():
    NumColours = False
    while(not NumColours):
        try:
            NumColours = int(
                input("Enter the number of colours you would like in your palette "))
            return NumColours
        except:
            print("Please input a valid number.")
            NumColours = False


def createFile():
    NumColours = getNumColours()
    colours = []
    check = False

    for i in range(NumColours):

        while (check != True):
            colourName = input("Enter the name of your colour: ")
            check = input(
                "Are you sure? Type Y or y for YES anything else will be taken as NO ")
            if('y' == check or 'Y' == check):
                check = True

        check = False

        while(check != True):
            suggestion = "Enter the hex code of the colour you want to call "+colourName + ". Do not add an Octothorpe(#). "
            HexCode = input(suggestion)
            check = input(
                "Are you sure? Type Y or y for YES anything else will be taken as NO ")
            if('y' == check or 'Y' == check):
                check = True
            else:
                check = False

        check = False
        a = (colourName, HexCode)
        colours.append(a)

    print(colours)

    filename = input(
        "What do you want this palette to be called?\n Do not add a .css to the end ") + ".css"
    cssfile = open(filename, "w+")

    cssCode = ""
    for colour in colours:
        cssCode += ".bg-"+colour[0] + "{background-color: #"+colour[1] + "}\n"
    for colour in colours:
        cssCode += ".border-"+colour[0] + \
            "{border: 1px solid #"+colour[1]+"}\n"

    cssfile.write(cssCode)
    cssfile.flush()
    cssfile.close()


createPalettes = True
print("Welcome. Let's create a colour palette.")
choice = input(
    "Shall we proceed?\nAnswer with y or Y for YES and any other letter for NO ")
if(choice != 'y' and choice != 'Y'):
    createPalettes = False

while(createPalettes):
    createFile()
    choice = input("Do you want to create more palettes to show your client?\nAnswer with y or Y for YES and any other letter for NO")
    if(choice != 'y' and choice != 'Y'):
        createPalettes = False