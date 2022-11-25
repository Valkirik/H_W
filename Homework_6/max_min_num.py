

def max_min_num(n: str) -> int:
    spl = n.split()
    spl.sort()
    for i in spl:
        if int(i) == 0:
            spl.remove(i)
    print(spl)

    rev = list(reversed(spl))
    for i in rev:
        if int(i) < 0:
            rev.remove(i)

    i =  "".join(spl), "".join(rev)

    return ", ".join(i)

print(max_min_num("1 9 3 4 -5"))













