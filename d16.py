baseSeq = (0,1,0,-1)
if __name__=="__main__":
    l = open("d16.in").readline().strip()[:]
    skip = int("".join(l[:7]))
    # n = l
    # N = len(n)
    # seq = {}
    # for i in range(1,N+1):
    #     s = []
    #     for j in baseSeq:
    #         s.extend([j] * i)
    #     seq[i-1] = s[:]

    # for p in range(100):
    #     v = []
    #     for i in range(N):
    #         _v = 0
    #         _s = seq[i]

    #         _n = len(_s)
    #         for i,_d in enumerate(n):
    #             x = _s[(i+1)%_n]
    #             _v += int(_d)*x
    #         v.append(str(_v)[-1])
    #     # print(v)
    #     n = v

    # print("".join(n[:8]))
    
    ll = list(map(int, l))
    ll *= 10000

    for _ in range(100):
        for i in reversed(range(skip, len(ll)-1)):
            ll[i] = (ll[i] + ll[i+1]) % 10

    print(ll[skip:(skip+8)])
            


        