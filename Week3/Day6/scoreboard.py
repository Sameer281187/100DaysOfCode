from turtle import Turtle
SCORE_ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=SCORE_ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=SCORE_ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()