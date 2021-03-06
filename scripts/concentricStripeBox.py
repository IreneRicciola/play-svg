"""creates a box in a box recursively, with alternating black and white fills to create a nested rectangle pattern"""

from playsvg.document import *
from playsvg.element import *
from playsvg.path import *
import os
import string



def makeCentredBox(docu, size):
    boxPath = PathData().moveTo(Point(size, size)).\
            lineTo(Point(size, -1*size)).\
            lineTo(Point(-1*size, -1*size)).\
            lineTo(Point(-1*size, size)).closePath()
    return boxPath

def makeStripeBox(docu, layers, layerSize):
    stripeBoxGroup = docu.makeGroup()
    for i in range(layers,0, -1):
        if i%2 == 0:
            stripeBoxGroup.append(buildPath(makeCentredBox(docu, i*layerSize),{'style': 'stroke:none;fill:black'})) 
        else:
            stripeBoxGroup.append(buildPath(makeCentredBox(docu, i*layerSize),{'style': 'stroke:none;fill:white'})) 
    return stripeBoxGroup    

docu = document.Document()
docu.append(makeStripeBox(docu,20, 20 ))

docu.writeSVG("concentricStripeBox.svg" )
print "done"

