from functools import reduce

def comp(a,b):
    if a[0]<b[0]:
        return a
    else:
        return b

if __name__=="__main__":
    data = [int(x) for x in open("d08.in").readline()[:]]
    layers = []
    freqs = []
    
    LS = 25*6
    N = len(data) // LS

    for i in range(N):
        layer = data[(i*LS):((i+1)*LS)][:]
        print(layer)
        layers.append(layer)
        f = (layer.count(0), layer.count(1), layer.count(2))
        print(f)
        freqs.append(f)

    freqs = reduce(comp, freqs)
    part1 = freqs[1]*freqs[2]
    print(part1)

    rr = []
    colors = {0:" ", 1:"#"}
    for i in range(LS):
        for j,l in enumerate(layers):
            if l[i] in set([0,1]):
                rr.append(colors[l[i]])
                break
    
    for i in range(6):
        print("".join(rr[(i*25):((i+1)*25)]))

