from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', True, align='center', font=('Arial', 14, 'normal'))
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align='center', font=('Arial', 14, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()