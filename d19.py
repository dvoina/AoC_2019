from intcode import intcode as ic
from collections import defaultdict


if __name__=="__main__":
    _memory = [0] * 64 * 1024 * 1024
    _data = [int(x) for x in open("d17.in").read().split(",")]
    _memory[0:len(_data)] = _data

    cpu = ic.CPU("Part1", _memory, ic.Queue(), ic.Queue())
    scr = [["."]*50 for _ in range(50)]
    count = 0
    for i in range(50):
        for j in range(50):
            cpu._in.put(j)
            cpu._in.put(i)
            cpu.interpret()
            d = chr(cpu._out.get())
            if d=='1':
                count +=1 
            scr[i][j] = d
    for l in scr:
        print("".join(l))
        
    print(count)



    

