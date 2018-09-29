import os, sys

import parsedalton
import parsegaussian
import molplot

print(sys.argv)
filename = sys.argv[1]

if filename.lower().endswith('gjf'): mol = parsegaussian.parsegif(filename)
elif filename.lower().endswith('log'): mol = parsegaussian.parselog(filename)
elif filename.lower().endswith('mol'): mol = parsedalton.parsemol(filename)
elif filename.lower().endswith('out'): mol = parsedalton.parseout(filename)

molplot.plot_molecule(mol)
