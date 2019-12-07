import itertools
from multiprocessing import Process, Queue
import time

class Operand(object):
    def __init__(self):
        self.data = None

    def get(self):
        return self.data

    def set(self, value):
        self.data = value

class Immediate(Operand):
    def __init__(self, value):
        Operand.__init__(self)
        self.data = value

class Address(Operand):
    def __init__(self, memory, address):
        Operand.__init__(self)
        self.memory = memory
        self.data = address

    def get(self):
        return self.memory[self.data]

    def set(self, value):
        self.memory[self.data] = value

class CPU(object):
    def __init__(self, name, memory, inQ, outQ):
        self.name = name
        self.memory = memory[:]
        self.ip = 0
        self._in = inQ
        self._out = outQ 


    def __fetch(self) -> tuple:
        return (self.memory[self.ip:self.ip+4])


    def __decode(self, instruction:tuple) -> tuple:
        modes, opcode = divmod(instruction[0],100)
        m3, modes = divmod(modes, 100)
        m2, modes = divmod(modes, 10)
        m1 = modes
        try:
            if m1 == 1:
                op1 = Immediate(instruction[1])
            else:
                op1 = Address(self.memory, instruction[1])

            if m2 == 1:
                op2 = Immediate(instruction[2])
            else:
                op2 = Address(self.memory, instruction[2])

            if m3 == 1:
                res = Immediate(instruction[3])
            else:
                res = Address(self.memory, instruction[3])

            return (opcode, op1, op2, res)
        except:
            print(instruction)


    def __execute(self, instruction:tuple) -> int:
        opcode, op1, op2, res = instruction
        
        if opcode == 1:
            res.set(op1.get() + op2.get())
            return self.ip+4
        
        if opcode == 2:
            res.set(op1.get() * op2.get())
            return self.ip+4
        
        if opcode == 3:
            op1.set(self._in.get())
            return self.ip + 2
        
        if opcode == 4:
            self._out.put(op1.get())
            return self.ip + 2
        
        if opcode == 5:
            if op1.get() != 0:
                return op2.get()
            else:
                return self.ip + 3
        
        if opcode == 6:
            if op1.get() == 0:
                return op2.get()
            else:
                return self.ip + 3
        
        if opcode == 7:
            if op1.get() < op2.get():
                res.set(1)
            else:
                res.set(0)
            return self.ip+4
        
        if opcode == 8:
            if op1.get() == op2.get():
                res.set(1)
            else:
                res.set(0)
            return self.ip+4

        if opcode == 99:
            return None

    def interpret(self) -> int:
        self.ip = 0
        while self.ip != None:
            self.ip = self.__execute(self.__decode(self.__fetch()))

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
            c = CPU("CPU_"+str(i), data, q1, q2)
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
            cc = CPU("CPU_"+str(i), _data, q[i], q[(i+1) % 5])
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
    
    #part1(_data)
    part2(_data)

 


