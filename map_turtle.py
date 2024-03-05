from turtle import Turtle
FONT = ('Courier', 10, 'normal')

class MapTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def right_answer(self, user_answer, new_x, new_y):
        self.goto(int(new_x.iloc[0]), int(new_y.iloc[0]))
        self.write(f"{user_answer}", font=FONT)

