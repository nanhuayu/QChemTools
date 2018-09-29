import os, sys

import parsedalton
import molplot

print(sys.argv)
filename = sys.argv[1]

mol = parsedalton.parseout(filename)
molplot.plot_molecule(mol)
