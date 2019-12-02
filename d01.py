import sys
import functools

def fuel(x):
    if x<=0:
        return 0
    else:
        return x + fuel(int(x/3)-2)

def part1(_in:[int]) -> int:
    return functools.reduce(lambda x,y: x+y, [int(x/3)-2 for x in _in])

def part2(_in:[int]) -> int:
    return functools.reduce(lambda x,y: x+y, [fuel(x)-x for x in _in])

if __name__=="__main__":
    inputs = [int(x) for x in open("d01.in").   readlines()]
    print(part1(inputs))
    print(part2(inputs))
