from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.our_score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.print_score()

    def game_over(self):
        self.goto(y=0, x=0)
        self.color("red")
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def print_score(self):
        self.write(f"Score: {self.our_score}", False, align=ALIGNMENT, font=FONT)
        self.our_score += 1
        # Depending on your score, the score display color will change accordingly
        if self.our_score < 36:
            self.color("white")
        elif self.our_score < 80:
            self.color("green")
        elif self.our_score < 160:
            self.color("yellow")
        else:
            self.color("red")
