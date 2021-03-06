"""Script for generating example of the output of compshapes.py functions 
See `compshapes.py <https://github.com/cosmo-guffa/play-svg/blob/master/playsvg/compshapes.py>`_ for more info on corresponding functions """

from playsvg.document import *
from playsvg import compshapes


docu = Document()
for i in range(7,13):
    docu.append(compshapes.buildHexagonLattice(12, 30, i*0.1 ))
docu.writeSVG("compshapes_hexagonal_lattice.svg")
