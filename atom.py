import json

with open('atominfo.json','r',encoding='utf8') as f:
    atominfo = json.loads(f.read())

class Atom:
    def __init__(self, x, y, z, name = 'H'):
        self.xyz = float(x),float(y),float(z)
        self.name = name
        self.color = self.get_color(self.name)
        self.size = self.get_size(self.name)
        self.number = self.get_number(self.name)

    def get_color(self, name):
        color = atominfo[name]["color"]
        return int(color[:2],16)/256, int(color[2:4],16)/256, int(color[4:],16)/256

    def get_size(self, name):
        size = atominfo[name]["size"]
        return float(size)

    def get_number(self, name):
        number = atominfo[name]["number"]
        return int(number)
