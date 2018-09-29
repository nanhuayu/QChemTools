import os

import atom

atomnum = ['1','6','7','8','16']
atomname = ['H','C','N','O','S']

def parsegjf(fn):
    with open(fn,'r',encoding='utf8') as f:
        fcontent = f.read()
    molcontent = fcontent.split("\n\n")[2]
    molstrlist = [[j for j in i.split(" ") if j]
                  for i in molstr.split('\n') if i][1:]
    molecule = [atom.Atom(i[1],i[2],i[3], i[0]) for i in molstrlist]
    return molecule

def parselog(fn):
    with open(fn,'r',encoding='utf8') as f:
        fcontent = f.read()
    molcontent = fcontent.split(" Number     Number       Type             X           Y           Z")[-1]
    molcontent = molcontent.split(" ---------------------------------------------------------------------")[1]
    molstrlist = [[j for j in i.split(" ") if j]
                  for i in molcontent.split('\n') if i]
    #for i in molstrlist:print(i)
    molstrlist = [[dict(zip(atomnum,atomname))[i[1]]]+i[3:] for i in molstrlist]
    molecule = [atom.Atom(i[1],i[2],i[3], i[0]) for i in molstrlist]
    return molecule

