#!/usr/bin/python

# ViperDisplayGenerator
# MFD Display Library

# Kurt Kochendarfer
# Sonoran Technology, LLC
# January 2016

class MFD:

    """This file contains basic structures needed to build any F-16 display"""

    def __init__(self):

        # This tuple contains the pertinent MFD status indicators (i.e. isSOI, mfdPage, etc.)  Initializes empty.
        self.status = ()

        # Sets the height/width of the MFD.  A standard F-16 CMFD is 4x4 inches. 
        self.height = 4
        self.width = 4

        # Sets the default font & font color for the MFD.  Change to your default standard, if needed.
        self.font = "H"
        self.fontColor = "yellow"

        # Creates the basic black MFD screen on which everything else will be displayed/overlayed. The created screen is the actual size of the MFD dimensions listed above. Use the pic "scale" vaiable to proportionally scale the display. 
        self.Screen = "Screen: box shaded \"black\" rad 0.2 height " + str(self.height) + " width " + str(self.width) + ";\n"

        # Defines the OSB positions around the screen display referenced to the center of the screen.  
        self.osbPos = {'1':'at Screen.c + (-1.3,2.2)','2':'at Screen.c + (-.65,2.2)','3':'at Screen.c + (0,2.2)','4':'at Screen.c + (.65,2.2)','5':'at Screen.c + (1.3,2.2)','6':'at Screen.c + (2.2,1.3)','7':'at Screen.c + (2.2,.65)','8':'at Screen.c + (2.2,0)','9':'at Screen.c + (2.2,-.65)','10':'at Screen.c + (2.2,-1.3)','11':'at Screen.c + (1.3,-2.2)','12':'at Screen.c + (.65,-2.2)','13':'at Screen.c + (0,-2.2)','14':'at Screen.c + (-.65,-2.2)','15':'at Screen.c + (-1.3,-2.2)','16':'at Screen.c + (-2.2,-1.3)','17':'at Screen.c + (-2.2,-.65)','18':'at Screen.c + (-2.2,0)','19':'at Screen.c + (-2.2,.65)','20':'at Screen.c + (-2.2,1.3)'}

        # Defines the OSB label positions around the screen display referenced to the center of the screen.
        self.labelPos = {'1':'at Screen.c + (-1.3,1.85)','2':'at Screen.c + (-.65,1.85)','3':'at Screen.c + (0,1.85)','4':'at Screen.c + (.65,1.85)','5':'at Screen.c + (1.3,1.85)','6':'at Screen.c + (1.75,1.3)','7':'at Screen.c + (1.75,.65)','8':'at Screen.c + (1.75,0)','9':'at Screen.c + (1.75,-.65)','10':'at Screen.c + (1.75,-1.3)','11':'at Screen.c + (1.3,-1.85)','12':'at Screen.c + (.65,-1.85)','13':'at Screen.c + (0,-1.85)','14':'at Screen.c + (-.65,-1.85)','15':'at Screen.c + (-1.3,-1.85)','16':'at Screen.c + (-1.75,-1.3)','17':'at Screen.c + (-1.75,-.65)','18':'at Screen.c + (-1.75,0)','19':'at Screen.c + (-1.75,.65)','20':'at Screen.c + (-1.75,1.3)'}        
    
    # This function creates the pic code to place OSBs around the edge of the screen.
    def makeOSB(self,num):

        try:
            button = "OSB" + str(num) + ": box rad 0.05 width 0.25 height 0.25 " + self.osbPos[str(num)] + ";\n"
            return button

        except KeyError:
            raise UserWarning("Invalid OSB number: " + str(num) + " (OSB numbers must be between 1-20)")

    # This function creates the pic code to place OSB labels on the screen.  This function automatically scales the label size based on the overall pic "scale" variable, since pic does not automatically scale fonts.
    def makeOSBLabel(self,num,label1,label2,backhl,twoln):

        try:
            labelStart = "\"\\f" + self.font+ "\\m[" + self.fontColor + "]"
            labelEnd = "\\m[]\\f[]\"" + self.labelPos[str(num)] + ";\n"
            label = labelStart + label1 + labelEnd
            return label

        except KeyError:
            raise UserWarning("Invalid OSB number: " + str(num) + " (OSB numbers must be between 1-20)")

#TODO
# 1) Create a label scaling function which scales label font according to the pic "scale" variable
# 2) Create backhighlight function/feature
# 3) Create SOI line between labels if display is SOI
# 4) Display two-line labels properly
# 5) Display 75% font two-line labels properly
# 6) Find correct display font

#-----------
display = MFD()
f = open('MFD.ms','w')
a = ""

for b in range(1,21):
    btn = display.makeOSB(b) + display.makeOSBLabel(b,"TEST","","y","n")
    a = a + btn

m = ".PS\n" + "scale = 1.2\n" + display.Screen + a + ".PE\n"
f.write(m)
f.close()


