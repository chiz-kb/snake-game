from turtle import Turtle, update

class ScoreBoard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.pu()
        self.pencolor('white')
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        with open('high_score.txt') as file:
            self.highscore=file.read()
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High score: {self.highscore}',move=False,align="center",font=('Arial',23,'normal'))
    def reset_scoreboard(self):
        if self.score>int(self.highscore):
            self.highscore=self.score
            with open('high_score.txt',mode='w') as file:
                file.write(str(self.highscore))
        self.score=0
        self.updatescore()
    
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(arg='Game Over',move=False,align="center",font=('Arial',23,'normal'))
    def increas_score(self):
            self.score+=1
            self.updatescore()
