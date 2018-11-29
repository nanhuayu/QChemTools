import os

import atom

def parsemol(fn):
    with open(fn,'r',encoding='utf8') as f:
        fcontent = f.read()
    molcontent = fcontent
    molstrlist = [[j for j in i.split() if j]
                  for i in molcontent.split('\n')[7:] if i and '=' not in i]
    molstrlist = [i for i in molstrlist if len(i) == 4]
    molecule = [atom.Atom(i[1], i[2], i[3], i[0]) for i in molstrlist]
    return molecule

def parseout(fn):
    with open(fn,'r',encoding='utf8') as f:
        fcontent = f.read()
    molcontent = fcontent.split("   Content of the .mol file")[-1]
    molcontent = molcontent.split("\n\n\n")[0]
    molstrlist = [[j for j in i.split() if j]
                  for i in molcontent.split('\n')[7:] if i and '=' not in i]
    molstrlist = [i for i in molstrlist if len(i) == 4]
    molecule = [atom.Atom(i[1], i[2], i[3], i[0]) for i in molstrlist]
    return molecule


if __name__ == '__main__':
    mol = parseout('C:\\Users\\nanhuayuipc\\Desktop\\tpa_ADTDB_OPT_6311.out')
