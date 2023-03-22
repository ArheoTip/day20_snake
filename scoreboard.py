from turtle import Turtle
ALIGNMENT ="center"
FONT = ('Arial', 20, 'normal')
# x

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.goto(0, 270)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def save_high_score(self):
    #     with open("high_scores.txt", "a") as f:
    #         f.write(f"\n{self.high_score}")
    #
    # def read_high_score(self):
    #     with open("high_scores.txt", "r+") as f:
    #         cont = f.read().strip()
    #         # old_high_score = int(f.readline().strip())
    #         if cont:
    #             self.high_score = cont
    #         else:
    #             self.high_score = 0

