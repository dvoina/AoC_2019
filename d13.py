import itertools
import time
import collections
from intcode import intcode as ic
from getkey import getkey, keys


if __name__=="__main__":
    _memory = [0] * 64 * 1024 * 1024
    _data = [int(x) for x in open("d13.in").read().split(",")]
    _memory[0:len(_data)] = _data

    outq = ic.Queue()
    c = ic.CPU("Part1", _memory, ic.Queue([1]), outq)
    c.interpret()
    sol = collections.defaultdict(int)
    for i in range(outq.len()//3):
        x,y,z =outq.data[(3*i):(3*i+3)]
        sol[(x,y)]=z
    n = 0
    for k in sol.keys():
        if sol[k]==2:
            n +=1
    print(n)

    DD = {
        0:" ", 1:"#", 2:"B", 3:"_",4:"O"
    }

    min_width = min(map(lambda x: x[0], sol.keys()))
    min_height = min(map(lambda x: x[1], sol.keys()))
    sol = {(x - min_width, y - min_height): v for (x, y), v in sol.items()}
    width = max(map(lambda x: x[0], sol.keys())) + 1
    height = max(map(lambda x: x[1], sol.keys())) + 1

    output = [[" "] * width for _ in range(height)]
    

    _memory[0] = 2
    while True:
        for (x, y), v in sol.items():
            output[y][x] = DD[v]

        for row in output:
            print("".join(row))
        key = getkey()
        if key==keys.LEFT:
            c._in.put(-1)
        if key==keys.RIGHT:
            c._in.put(1)
        c.interpret()
        for i in range(outq.len()//3):
            x,y,z =outq.data[(3*i):(3*i+3)]
            sol[(x,y)]=z

