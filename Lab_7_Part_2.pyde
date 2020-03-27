'''
Haruka Kido
ID #1323392
haruka.kido@ndus.edu
CSci 160. Weekly Lab 7. Part 2
Initial Functions Using Processing
'''

def setup():
    size (675, 300)
    background (myDarkTorquoise)
    
myDarkTorquoise = color (0, 128, 128)
myBlack = color (0, 0, 0)
myRed = color (130, 0, 0)

def draw():
    drawA()
    drawR()
    drawT()
    drawShadowedA()
    drawShadowedR()
    drawShadowedT()
    
A = "A"
def drawA():
    textSize (260)
    text (A, 65, 235)
    fill (myBlack)
    stroke (myBlack)
    
def drawShadowedA():
    textSize (260)
    text (A, 80, 245)
    fill (myRed)
    stroke (myRed)

R = "R"
def drawR():
    text (R, 275, 235)
    fill (myBlack)
    stroke (myBlack)
    
def drawShadowedR():
    text (R, 292, 245)
    fill (myRed)
    stroke (myRed)
    
T = "T"
def drawT():
    text (T, 450, 235)
    fill (myRed)
    stroke (myRed) 
    
def drawShadowedT():
    text (T, 468, 245)
    fill (myBlack)
    stroke (myBlack)
