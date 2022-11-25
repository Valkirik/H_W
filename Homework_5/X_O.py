


def x_o(n: str) -> str:
    a = n.count("x")
    b = n.count("o")

    for i in n.split():
        if a == b:
            print("true")
        elif a == 0 or b == 0:
            print("true")
        else: print("false")

x_o("xoo")





