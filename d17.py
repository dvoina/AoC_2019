from intcode import intcode as ic
from collections import defaultdict


if __name__=="__main__":
    _memory = [0] * 4 * 1024 * 1024
    _data = [int(x) for x in open("d17.in").read().split(",")]
    _memory[0:len(_data)] = _data

    cpu = ic.CPU("Part1", _memory, ic.Queue(), ic.Queue())
    cpu.interpret()
    data = "".join([chr(x) for x in cpu._out.data]).strip().split("\n")
    print(data)
    s = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if data[i][j]=="#" and data[i-1][j]=="#"and data[i+1][j]=="#" and data[i][j-1]=="#" and data[i][j+1]=="#":
                s += (i*j)
    print(s)


    

