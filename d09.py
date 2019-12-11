import itertools
import time
from intcode import intcode as ic

if __name__=="__main__":
    _memory = [0] * 64 * 1024 * 1024
    _data = [int(x) for x in open("d09.in").read().split(",")]
    #_data = [int(x) for x in "1102,34915192,34915192,7,4,7,99,0".split(",")]
    _memory[0:len(_data)] = _data

    outq = ic.Queue()
    c = ic.CPU("Part1", _memory, ic.Queue([1]), outq)
    c.interpret()
    print(outq.get())
    c = ic.CPU("Part2", _memory, ic.Queue([2]), outq)
    c.interpret()
    print(outq.get())



