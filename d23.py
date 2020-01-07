from intcode import intcode as ic
from collections import defaultdict
import multiprocessing as mp

code = None

def runvm(_cpu:ic.CPU) -> None:
    print("starting:", i)
    _cpu.interpret()
    print("done", i)


if __name__=="__main__":
    _memory = [0] * 4 * 1024 * 1024
    _data = [int(x) for x in open("d23.in").read().split(",")]
    _memory[0:len(_data)] = _data
    code = _memory
    cpus = []
    queues = []
    for i in range(50):
        q = (mp.Queue(), mp.Queue())
        queues.append(q)
        _cpu = ic.CPU(str(i), _memory, q[0], q[1])
        w = mp.Process(target=runvm, args=(_cpu,)) 
        cpus.append(w)
        w.start()
    packets = []
    while True:
        for i in range(50):
            print(".",)
            if not queues[i][1].empty():
                p = queues[i][1].get_nowait()
                print(".",)
                if p==255:
                    print(queues[i][1].get())
                    exit(0)
                x = q[i][1].get()
                print("{} -> {} {}".format(i, p, x))



