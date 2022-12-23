class Snow:
    def __init__(self, snowflake_count: int):
        self.snowflake_count = snowflake_count

    def __add__(self, other):
        self.snowflake_count + other


    def __mul__(self, other):
        self.snowflake_count * other

    def __sub__(self, other):
        self.snowflake_count - other

    def __truediv__(self, other):
        self.snowflake_count / other


    def make_snow(self, snowflake_array: int):
        array_count = self.snowflake_count // snowflake_array
        for _ in range(array_count):
            print("*" * snowflake_array)

snow = Snow(100)
snow.make_snow(10)
