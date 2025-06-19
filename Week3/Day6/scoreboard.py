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
        self.high_score = self.get_current_high_score("high_score.txt")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=SCORE_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_high_score_to_file("high_score.txt", self.high_score)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=SCORE_ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.update_scoreboard()

    def write_high_score_to_file(self, filename, score):
        with open(filename, "w") as high_score_file:
            high_score_file.write(str(score))

    def get_current_high_score(self, filename):
        with open(filename, "r") as high_score_file:
            high_score = high_score_file.read()
            return int(high_score)