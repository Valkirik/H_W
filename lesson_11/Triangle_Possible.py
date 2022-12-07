class Triangle:
    def __init__(self, side_list):
        self.side_list = side_list


    def get_possibility(self):
        a = self.side_list[0]
        b = self.side_list[1]
        c = self.side_list[2]

        l = [a, b, c]

        list_min = [i for i in l if i < max(l)]

        if sum(list_min) <= max(l):
            return ("It is impossible to build a triangle")
        else:
            return ("It is possible to build a triangle")

triangle_1 = Triangle([2, 2, 3])

print(triangle_1.get_possibility())






"""def mwx(a, b ,c):
    e = [a, b, c]

    m = max(list(e))
    l = [i for i in list(e) if i < m]

    if sum(l) <= m:
        return("impossible")

    else: return("possible")


print(mwx(3, 5, 4))"""

















