from collections import defaultdict
import math

def alchemy(fuel):
    requires = defaultdict(int, {"FUEL": -fuel})
    todo = ["FUEL"]

    while todo:
        ele = todo.pop()
        needed = -requires[ele]
        produced, inp = formula[ele]
        repeat = math.ceil(needed / produced)
        requires[ele] += repeat * produced

        for amt, ele in inp:
            requires[ele] -= amt * repeat
            if ele != "ORE" and requires[ele] < 0:
                todo.append(ele)

    return -requires["ORE"]


if __name__=="__main__":
    data = [x.strip().split("=>") for x in open("d14.in").readlines()]
    formula = {}
    for j,d in enumerate(data):
        i,r = d
        i = [tuple(_i.strip().split(" ")) for _i in i.split(",")]
        i = [(int(x[0]), x[1]) for x in i]
        r = tuple(_r.strip() for _r in r.strip().split(" "))
        r = (int(r[0]), r[1])
        formula[r[1]] = (r[0], i)
    print(formula)
    print(alchemy(1))
    minF = 10 ** 12 // alchemy(1)
    maxF = minF * 10

    while minF != maxF:
        fuel = (minF + maxF + 1) // 2
        if alchemy(fuel) > 10 ** 12:
            maxF = fuel - 1
        else:
            minF = fuel

    print("Part 2:", maxF)
