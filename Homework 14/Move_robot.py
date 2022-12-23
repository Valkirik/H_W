class Robot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def move(self, n: str):
        new_x = self.x
        new_y = self.y
        for i in n:
            match i:
                case "W":
                    new_y += 1
                    if new_y not in range(0, 101):
                        return "Robot can not move in this way"
                case "S":
                    new_y -= 1
                    if new_y not in range(0, 101):
                        return "Robot can not move in this way"
                case "D":
                    new_x += 1
                    if new_x not in range(0, 101):
                        return "Robot can not move in this way"
                case "A":
                    new_x -= 1
                    if new_x not in range(0, 101):
                        return "Robot can not move in this way"


        self.x = new_x
        self.y = new_y
        return self.x, self.y

robot = Robot(0, 0)
print(robot.move("WDA"))




        

















