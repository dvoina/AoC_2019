baseSeq = (0,1,0,-1)
if __name__=="__main__":
    n = [int(d) for d in open("d16.in").readline().strip()[:]]


    N = len(n)
    seq = {}
    for i in range(1,N+1):
        s = []
        for j in baseSeq:
            s.extend([j] * i)
        seq[i-1] = s[:]
    for p in range(100):
        v = []
        for i in range(N):
            _v = 0
            _s = seq[i]

            _n = len(_s)
            for i,_d in enumerate(n):
                x = _s[(i+1)%_n]
                _v += _d*x
            v.append(abs(_v)%10)
        # print(v)
        n = v
    print("".join(n[:8]))
        
            


        