from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self, screenheight):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(0, screenheight - 20)
        self.update_score()

    # for printing the score
    def update_score(self):
        self.write(f'SCORE: {self.score}', align=ALIGNMENT, font=FONT)

    # for writing GAME OVER when game ends
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    # incrementing score on the screen
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
