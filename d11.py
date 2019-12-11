from intcode import intcode as ic
from collections import defaultdict
import multiprocessing as mp

def runvm(vm, _in, _out):
    vm.interpret()

def paint(code, start):
    image = defaultdict(int)
    x, y = 0, 0
    image[(x, y)] = start
    direction = 0
    _in = mp.Queue()
    _out = mp.Queue()
    vm = ic.CPU("Part1", code, _in, _out)
    w = mp.Process(target=runvm, args=(vm, _in, _out))
    w.start()

    while w.is_alive():
        _in.put(image[(x, y)])
        color = _out.get()
        turn = _out.get()
        image[(x, y)] = color
        direction = (direction + turn * 2 - 1) % 4
        x += (0, 1, 0, -1)[direction]
        y += (-1, 0, 1, 0)[direction]
        if (x,y)==(41,4):
            break
    w.terminate()
    return image

if __name__=="__main__":
    _memory = [0] * 64 * 1024 * 1024
    _data = [int(x) for x in open("d11.in").read().split(",")]
    _memory[0:len(_data)] = _data

    #print(len(paint(_memory, 0)))

    image = paint(_memory, 1)
    min_width = min(map(lambda x: x[0], image.keys()))
    min_height = min(map(lambda x: x[1], image.keys()))

    image = {(x - min_width, y - min_height): v for (x, y), v in image.items()}
    width = max(map(lambda x: x[0], image.keys())) + 1
    height = max(map(lambda x: x[1], image.keys())) + 1

    output = [[" "] * width for _ in range(height)]

    for (x, y), v in image.items():
        if v == 1:
            output[y][x] = "#"

    for row in output:
        print("".join(row))