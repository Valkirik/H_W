class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_possibility(self):
        e = [self.a, self.b, self.c]

        list_min = [i for i in list(e) if i < max(list(e))]

        if sum(list_min) <= max(list(e)):
            return ("It is impossible to build a triangle")
        else:
            return ("It is possible to build a triangle")

triangle_1 = Triangle(a = 2, b = 1, c = 4)

print(triangle_1.get_possibility())























