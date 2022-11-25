def camle_case(n: str) -> str:
    i = n.split("-")
    t = n.split("_")

    if "-" in n:
        print("".join(map(lambda word: word.capitalize(), i)))
    else:
        print("".join(map(lambda word: word.capitalize(), t)))

print(camle_case("the-stealth-warrior"))















"""u = ["cat", "map"]
w_up = list(map(lambda word: word.capitalize(), u))
q = ("".join(w_up))
print(q)"""



