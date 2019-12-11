import itertools
from multiprocessing import Process, Queue
import time
from intcode import intcode as ic


def interpret_mp(c, inQ, outQ) -> int:
    print("starting "+c.name)
    c.interpret()
    print("done "+c.name)


def part1(data):
    #part1
    phases = list(itertools.permutations([0,1,2,3,4]))
    sol = []
    for p in phases:
        _s = 0
        for i in range(5):
            q1 = Queue()
            q1.put(p[i])
            q1.put(_s)
            q2 = Queue()
            c = ic.CPU("CPU_"+str(i), data, q1, q2)
            c.interpret()
            _s = q2.get()
        sol.append(_s)
    print(max(sol))

def part2(data):
    #part2
    phases = list(itertools.permutations([5,6,7,8,9]))
    sol = []
    for p in phases:
        _s = 0
        q = []
        c = []
        j = []
        for i in range(5):
            _q = Queue()
            _q.put(p[i])
            q.append(_q)
        q[0].put(0)
        for i in range(5):
            cc = ic.CPU("CPU_"+str(i), _data, q[i], q[(i+1) % 5])
            w = Process(target = interpret_mp, args=(cc, q[i], q[(i+1) % 5]))
            c.append(cc)
            j.append(w)
            w.start()
        while len(j)>0:
            j = [jj for jj in j if jj.is_alive()]
            time.sleep(0.1)
        sol.append(c[4]._out.get())
        print("------------------")
    print(max(sol))

if __name__=="__main__":
    _data = [int(x) for x in open("d07.in").read().split(",")]
    _data.extend([99] * 4)
    
    part1(_data)
    part2(_data)

 


