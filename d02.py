def fetch(data:[int], ip:int) -> tuple:
    return (data[ip:ip+4])

def execute(instruction:tuple) -> int:
    operation, adr1, adr2, res = instruction
    if operation == 1:
        data[res] = data[adr1] + data[adr2]
        return 4
    if operation == 2:
        data[res] = data[adr1] * data[adr2]
        return 4
    if operation == 99:
        return 1

def interpret(data:[int]) -> int:
    ip = 0
    while True:
        instruction = fetch(data, ip)
        next = execute(instruction)
        if next == 1:
            break
        else:
            ip += next
    return data[0]

if __name__=="__main__":
    _data = [int(x) for x in open("d02.in").read().split(",")]
    
    #part 1
    data = _data[:]
    data[1] = 12
    data[2] = 2
    print(interpret(data))

    #part 2
    for i in range(100):
        for j in range(100):
            data = _data[:]
            data[1] = i
            data[2] = j
            r = interpret(data)
            if r == 19690720:
                print(r, 100*i+j)
            

