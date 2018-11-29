import os, sys
import json
import numpy as np

##filename = 'atominfo.json'
##with open(os.path.join(sys.path[0],filename),'r',encoding='utf8') as f:
##    atominfo = json.loads(f.read())
filename = os.path.join(sys.path[0],'atom.csv')
atominfo = np.genfromtxt(filename, encoding='utf8', dtype=None,
                    names=('number','name','info','radius','color'))

class Atom:
    def __init__(self, x, y, z, name = 'H'):
        self.xyz = float(x),float(y),float(z)
        self.name = name
        self.color = self.get_color(self.name)
        self.size = self.get_size(self.name)
        self.number = self.get_number(self.name)

    def get_color(self, name):
##        color = atominfo[name]["color"]
        index = int(np.argwhere(atominfo['name']==name))
        color = atominfo['color'][index]
        return int(color[:2],16)/256, int(color[2:4],16)/256, int(color[4:],16)/256

    def get_size(self, name):
##        size = atominfo[name]["size"]
        index = int(np.argwhere(atominfo['name']==name))
        size = atominfo['radius'][index]/100
        return float(size)

    def get_number(self, name):
##        number = atominfo[name]["number"]
        index = int(np.argwhere(atominfo['name']==name))
        number = atominfo['number'][index]
        return int(number)
