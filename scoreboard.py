from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "bold"))

    def left_scores(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()