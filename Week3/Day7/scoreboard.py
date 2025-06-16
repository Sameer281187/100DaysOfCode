from turtle import Turtle
SCORE_ALIGNMENT = "center"
FONT = ('Arial', 48, 'bold')
class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.write_scorecard()

    def write_scorecard(self):
        self.write(f"{self.score}", align=SCORE_ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write_scorecard()
