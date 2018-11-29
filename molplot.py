import numpy as np
from mayavi import mlab


def judge_line(xyzlist):
    retlist = set()
    sortlist = np.argsort(xyzlist)
##    print(sortlist)
    for idx in range(len(xyzlist)):
        for jdx in range(idx+1, len(xyzlist)):
            if xyzlist[sortlist[idx]] < xyzlist[sortlist[jdx]] - 2.0: break
            retlist.add((max(sortlist[idx],sortlist[jdx]),min(sortlist[idx],sortlist[jdx])))
    return retlist

def get_line(mol):
    length = lambda a,b: (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2
    line = lambda a,b: np.array(list(zip(a, b)))#(np.linspace(a[0],b[0],30),np.linspace(a[1],b[1],30),np.linspace(a[2],b[2],30))
    
    xyzlist = np.array([i.xyz for i in mol])
    idxlist = judge_line(xyzlist[:,0]) | judge_line(xyzlist[:,1]) | judge_line(xyzlist[:,2])
##    print(idxlist)
    retlist = [line(xyzlist[idx[0]],xyzlist[idx[1]])
               for idx in idxlist
               if length(xyzlist[idx[0]],xyzlist[idx[1]])<(mol[idx[0]].size+mol[idx[1]].size+0.5)**2]
    
    return retlist



def plot_line(idx, mol):
##    print(idx)
    ret = []
    line = lambda a,b: np.linspace(a,b,100)
    length = lambda a,b: (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2
    for midx, m in enumerate(mol):
        if idx == midx: continue
        if length(m.xyz, mol[idx].xyz) < 3.2:
            x,y,z = line(m.xyz[0], mol[idx].xyz[0]), line(m.xyz[1], mol[idx].xyz[1]), line(m.xyz[2], mol[idx].xyz[2])
            plot3d(x, y, z)
            ret.append((x,y,z))
    return ret


def plot_molecule(mol):
    line = get_line(mol)
    print(len(line))
    for l in line:
        mlab.plot3d(*l)
    for idx,m in enumerate(mol):
##        line += plot_line(idx, mol)
##        points3d(float(m[1]), float(m[2]), float(m[3]), resolution=12)
        mlab.points3d(*m.xyz, color=m.color, scale_factor=m.size, resolution=10)#,opacity=0.95)
        #mlab.text3d(m.xyz[0]+0.5,m.xyz[1]+0.5,m.xyz[2]+0.5, text=str(idx),scale=0.2)
    mlab.show()


if __name__ == '__main__':
    import parsegaussian
    mol = parsegaussian.parselog('BDTDB_syn_OPT_pm7.gjf')
    plot_molecule(mol)
