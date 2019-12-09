import itertools
import time

class Queue(object):
    def __init__(self, data = []):
        self.data = data

    def put(self, x):
        self.data.append(x)

    def get(self):
        return self.data.pop(0)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

class Operand(object):
    pass
        

class Immediate(Operand):
    def __init__(self, value):
        Operand.__init__(self)
        self.data = value

    def get(self):
        return self.data

    def set(self, value):
        self.data = value

    def __str__(self):
        return "#{}".format(self.data)


class Address(Operand):
    def __init__(self, memory, address):
        Operand.__init__(self)
        self.memory = memory
        self.address = address

    def get(self):
        return self.memory[self.address]

    def set(self, value):
        self.memory[self.address] = value

    def __str__(self):
        return "@({})".format(self.address)

class RelativeAddress(Address):
    def __init__(self, memory, base, address):
        Address.__init__(self, memory, address)
        self.memory = memory
        self.base = base
        self.address= address

    def get(self):
        return self.memory[self.base + self.address]

    def set(self, value):
        self.memory[self.base + self.address] = value

    def __str__(self):
        return "@({} + {})".format(self.base, self.address)

class CPU(object):
    MNEMOS = {1:"add", 2:"mul", 3:"in", 4:"out", 5:"jnz", 6:"jz", 7:"lt", 8:"eq", 9:"sb", 99:"halt"}

    def __init__(self, name, memory, inQ, outQ, debug = False):
        self.name = name
        self.memory = memory[:]
        self.ip = 0
        self._in = inQ
        self._out = outQ 
        self.base = 0
        self.debug = debug


    def __fetch(self) -> tuple:
        return (self.memory[self.ip:self.ip+4])


    def __decode(self, instruction:tuple) -> tuple:
        modes, opcode = divmod(instruction[0],100)
        m3, modes = divmod(modes, 100)
        m2, modes = divmod(modes, 10)
        m1 = modes
        try:
            op1, op2, res = None, None, None
            if m1 == 2:
                op1 = RelativeAddress(self.memory, self.base, instruction[1])
            if m1 == 1:
                op1 = Immediate(instruction[1])
            if m1 == 0:
                op1 = Address(self.memory, instruction[1])

            if m2 == 2:
                op2 = RelativeAddress(self.memory, self.base, instruction[2])
            if m2 == 1:
                op2 = Immediate(instruction[2])
            if m2 == 0:
                op2 = Address(self.memory, instruction[2])

            if m3 == 2:
                res = RelativeAddress(self.memory, self.base, instruction[3])
            if m3 == 1:
                res = Immediate(instruction[3])
            if m3 == 0:
                res = Address(self.memory, instruction[3])

            return (opcode, op1, op2, res)
        except:
            print(instruction)


    def __execute(self, instruction:tuple) -> int:
        opcode, op1, op2, res = instruction
        if self.debug:
            print("{} {} {} {}".format(CPU.MNEMOS[opcode], op1, op2, res))
        
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

        if opcode == 9:
            self.base += op1.get()
            return self.ip + 2
        
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


if __name__=="__main__":
    _memory = [0] * 64 * 1024 * 1024
    _data = [int(x) for x in open("d09.in").read().split(",")]
    #_data = [int(x) for x in "1102,34915192,34915192,7,4,7,99,0".split(",")]
    _memory[0:len(_data)] = _data

    outq = Queue()
    c = CPU("Part1", _memory, Queue([1]), outq)
    c.interpret()
    print(outq.get())
    c = CPU("Part1", _memory, Queue([2]), outq)
    c.interpret()
    print(outq.get())



