import itertools
import re

class Moon(object):
    def __init__(self, x,y,z):
        self.pos = [int(x),int(y),int(z)]
        self.vel = [0,0,0]
    def __repr__(self):
        return "pos=<{}> vel=<{}>".format(self.pos, self.vel)
    def __eq__(self, other):
        return self.vel==other.vel and self.pos==other.pos

def toMoon(s:str) -> dict:
    RE = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
    m = RE.match(s)
    if m != None:
        return Moon(m.group(1), m.group(2), m.group(3))
    return None

def applyGravity(m1:Moon, m2:Moon):
    for i in range(3):
        if m1.pos[i] < m2.pos[i]:
            m1.vel[i] += 1
            m2.vel[i] -= 1
        if m1.pos[i] > m2.pos[i]:
            m1.vel[i] -= 1
            m2.vel[i] += 1

def applyVelocity(m:Moon):
    for i in range(3):
        m.pos[i] += m.vel[i]

def energy(m:Moon):
    p = sum([abs(x) for x in m.pos])
    k = sum([abs(x) for x in m.vel])
    return p*k

if __name__=="__main__":
    moons = [toMoon(x.strip())  for x in open("d12.in").readlines()]
    im = [Moon(m.pos[0],m.pos[1],m.pos[2]) for m in moons]
    combs = list(itertools.combinations(range(4), 2))

    for i in range(1000):
        for c in combs:
            x,y = moons[c[0]], moons[c[1]]
            applyGravity(x, y)
        for m in moons:
            applyVelocity(m)
    e = sum([energy(m) for m in moons])
    print(e)




