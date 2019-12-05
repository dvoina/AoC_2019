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


def fetch(data:[int], ip:int) -> tuple:
    return (data[ip:ip+4])


def decode(instruction:tuple, memory:[int]) -> tuple:
    modes, opcode = divmod(instruction[0],100)
    m3, modes = divmod(modes, 100)
    m2, modes = divmod(modes, 10)
    m1 = modes
    
    if m1 == 1:
        op1 = Immediate(instruction[1])
    else:
        op1 = Address(memory, instruction[1])

    if m2 == 1:
        op2 = Immediate(instruction[2])
    else:
        op2 = Address(memory, instruction[2])

    if m3 == 1:
        res = Immediate(instruction[3])
    else:
        res = Address(memory, instruction[3])

    return (opcode, op1, op2, res)


def execute(instruction:tuple, ip) -> int:
    opcode, op1, op2, res = instruction
    
    if opcode == 1:
        res.set(op1.get() + op2.get())
        return ip+4
    
    if opcode == 2:
        res.set(op1.get() * op2.get())
        return ip+4
    
    if opcode == 3:
        op1.set(int(input("> ")))
        return ip + 2
    
    if opcode == 4:
        print("< {}".format(op1.get()))
        return ip + 2
    
    if opcode == 5:
        if op1.get() != 0:
            return op2.get()
        else:
            return ip + 3
    
    if opcode == 6:
        if op1.get() == 0:
            return op2.get()
        else:
            return ip + 3
    
    if opcode == 7:
        if op1.get() < op2.get():
            res.set(1)
        else:
            res.set(0)
        return ip+4
    
    if opcode == 8:
        if op1.get() == op2.get():
            res.set(1)
        else:
            res.set(0)
        return ip+4

    if opcode == 99:
        return None


def interpret(data:[int]) -> int:
    ip = 0
    while ip != None:
        ip = execute(decode(fetch(data, ip), data), ip)

    

if __name__=="__main__":
    _data = [int(x) for x in open("d05.in").read().split(",")]
    
    #part 1
    data = _data[:]
    print(interpret(data))
    # mem =  [1002,4,3,4,33]
    # execute(decode((mem[0:4]), mem))
    # print(mem)