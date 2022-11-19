

def simple_num(n: int) -> str:
    l = list(range(2, int(n)+1))
    count = [i for i in l if int(n) % int(i) == 0]

    if len(count) < 2:
        print("true")
    else: print("false")

simple_num(97)

