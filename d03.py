def bw(x,a,b):
    return min(a,b)<=x and x<=max(a,b)
def intersect(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    c = bw(x, line1[0][0], line1[1][0]) and bw(y, line1[0][1], line1[1][1]) and \
        bw(x, line2[0][0], line2[1][0]) and bw(y, line2[0][1], line2[1][1]) 
    if not c:
        raise Exception('lines do not intersect')
    return x, y

def part1(paths, ints):
    lines = []
    for p in paths:
        ll = []
        x = 0
        y = 0
        for m in p:
            d,q = m[0].upper(), int(m[1:])
            if d=="U":
                l = ((x, y), (x, y+q))
                y = y + q

            if d=="D":
                l = ((x, y), (x, y-q))
                y = y - q
                
            if d=="L":
                l = ((x, y), (x-q, y))
                x = x - q

            if d=="R":
                l = ((x, y), (x+q, y))
                x = x + q

            ll.append(l)
        lines.append(ll)

    for l1 in lines[0]:
        for l2 in lines[1]:
            try:
                ints.append(intersect(l1, l2))
            except Exception:
                pass
    dists = [abs(x[0])+abs(x[1]) for x in ints[1:]]
    print(min(dists))

def part2(paths, ints):
    ss = {}
    for x in ints:
        ss[x] = 0
    for p in paths:
        x = 0
        y = 0
        steps = 0
        s = {} 
        for m in p:
            d,q = m[0].upper(), int(m[1:])
            if d=="U":
                for _y in range(q):
                    y += 1
                    steps +=1
                    if (x,y) in ints:
                        if s.get((x,y)) == None: s[(x,y)]=steps

            if d=="D":
                for _y in range(q):
                    y -= 1
                    steps += 1
                    if (x,y) in ints:
                        if s.get((x,y)) == None: s[(x,y)]=steps
                
            if d=="L":
                for _x in range(q):
                    x -= 1
                    steps += 1
                    if (x,y) in ints:
                        if s.get((x,y)) == None: s[(x,y)]=steps

            if d=="R":
                for _x in range(q):
                    x += 1
                    steps += 1
                    if (x,y) in ints:
                        if s.get((x,y)) == None: s[(x,y)]=steps
        for x in ints:
            ss[x] += s[x]
    print(min(ss.values()))

if __name__=="__main__":
    paths = [x.split(",") for x in open("d03.in").readlines()]
    ints = []
    part1(paths, ints)
    part2(paths, ints)





    



