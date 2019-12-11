import math
import collections

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def angle(a,b):
    return math.atan2(b[1]-a[1], b[0]-a[0])

if __name__=="__main__":
    _data = [ l for l in open("d10.in").readlines()]
    a = []
    visible = {}

    for i,l in enumerate(_data):
        for j,c in enumerate(l):
            if c=="#":
                a.append((j,i))

    n = len(a)

    lut={(i,j):(angle(a[i],a[j]), dist(a[i], a[j])) for i in range(n) for j in range(n) if i!=j}

    _m = 0
    _p = None
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            count = 0
            for k in range(n):
                if i==k or j==k:
                    continue
                if lut[(i,k)]==lut[(k,j)]:
                    count += 1
            if count > _m:
                _m = count
                _p = i

    print(_m, _p)

