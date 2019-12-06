from collections import defaultdict


def countOrbits(p, parents, n):
    if p==None:
        return n-1
    else:
        return countOrbits(parents.get(p), parents, n+1)


def part1(data):
    parents = {}
    
    for p in data:
        parents[p[1]] = p[0]

    sum = 0
    for p in parents:
        sum += countOrbits(p, parents, 0)
    
    print(sum)
    
    
def path(s, parents, p):
    if s == None:
        return p
    else:
        p.append(s)
        return path(parents.get(s), parents, p)

def part2(data):
        parents = {}
        
        for p in data:
            parents[p[1]] = p[0]
        
        p1 = path("YOU", parents, [])
        p1.reverse()
        p2 = path("SAN", parents, [])
        p2.reverse()

        while p1[0]==p2[0]:
            p1.pop(0)
            p2.pop(0)

        print(len(p1)+len(p2)-2)


if __name__=="__main__":
    data = [tuple(x.strip().split(")")) for x in open("d06.in").readlines()]
    
    part1(data)
    part2(data)

