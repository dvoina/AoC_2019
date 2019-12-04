from collections import defaultdict

def check(n):
    cond = False
    for i in range(5):
        if n[i]==n[i+1]:
            cond = True
    return cond

def part1():
    count = 0
    for i in range (246540,787419):
        num = [int(x) for x in str(i)]
        cond = True
        for x in range(5):
            if num[x]>num[x+1]:
                cond = False
                break
        if cond==False:
            continue
        if not(check(num)):
            continue
        count = count + 1
    print(count)
    
def part2():
    count = 0
    for i in range (246540,787419):
        num = [int(x) for x in str(i)]
        cond = True
        for x in range(5):
            if num[x]>num[x+1]:
                cond = False
                break
        if cond==False:
            continue
        if not(check(num)):
            continue
        #finally found the catch
        cond = True
        d = defaultdict(int)
        for digit  in num:
            d[digit] += 1
        if not 2 in d.values():
            continue
        count = count + 1
    print(count)

if __name__=="__main__":
    part1()
    part2()
