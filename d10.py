import math
import collections

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def angle(a,b):
    return math.atan2(b[1]-a[1], b[0]-a[0])

if __name__=="__main__":
    _data = [ l for l in open("d10.in").readlines()]
    asteroids = []
    visible = {}

    for i,l in enumerate(_data):
        for j,c in enumerate(l):
            if c=="#":
                asteroids.append((j,i))

    n = len(asteroids)
    lut = {(a1, a2):(angle(a1,a2), dist(a1,a2)) for a1 in asteroids for a2 in asteroids if a1 != a2}
    #count = {}
    #for a,b in lut.keys():
    #    for x in asteroids:
    #        if x != a and x != b and lut[(a,b)][0]==lut[(a,x)][0] and lut[(a,x)][1]<=lut[(a,b)][1]:
    #            if count.get(a) == None:
    #                count[a] = 1
    #            else: 
    #                count[a] = count[a] + 1   
    #_max = 0

    _max = 0
    _pos = None
    for pos in asteroids:
        x, y = pos
        count = 0
        angles = {(ax, ay): math.atan2(ay - y, ax - x) for ax, ay in asteroids}
        for a in asteroids:
            for b in asteroids:
                if angles[a] == angles[b] and dist(a, pos) > dist(b, pos):
                    break
            else:
                count += 1
        if count > _max:
            _max = count
            _pos = pos
    print(_max, _pos)

    #p = None
    #for k in count.keys():
    #    v = count[k]
    #    if v>=_max:
    #        _max = v
    #        p = k
    #print(p, _max)


