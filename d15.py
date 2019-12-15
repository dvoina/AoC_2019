from intcode import intcode as ic
from collections import defaultdict

moves = {0: (0,0), 1:(0, -1), 2:(0,1), 3:(-1, 0), 4:(1,0)}
revs = {0:0, 1:2, 2:1, 3:4, 4:3}

def search(m, crt, l, vm):
    if m.get(crt) in ["#", "*"]:
        return 
    if int(m.get(crt))<l:
        return
    for _m in moves.keys():
        vm._in.put(_m)
        vm.interpret()
        p = vm._out.get()
        n = (crt[0] + moves[_m][0], crt[1] + moves[_m][1])
        if p==0:
            m[n] = "#"
        if p==1:
            if m.get(n) == None:
                m[n] = str(l+1)
            search(m,n,l+1,vm)
            vm._in.put(revs[_m])
            vm.interpret()
            vm._out.get()
        if p==2:
            m[crt]="*"
            print(l)


if __name__=="__main__":
    _memory = [0] * 4 * 1024 * 1024
    _data = [int(x) for x in open("d15.in").read().split(",")]
    _memory[0:len(_data)] = _data


    _in = ic.Queue()
    _out = ic.Queue()
    vm = ic.CPU("Part1", _memory, _in, _out)

    N=60
    crt = (N,N)
    l = 0
    m = {crt:"0"}
    search(m, crt, 0, vm)

    #print(m)
    img = [[" "]*(2*N) for _ in range(2*N)]
    for k in m.keys():
        x,y = k
        v = m[k]
        if v==0:
            v = " "
        if v not in ["*", "#"] and int(v)>0:
            v="."
        img[y][x] = v

    for y in img:
        print("".join(y))
    

