
class Snake:
    from turtle import Turtle
    def __init__(self):
        self.creat_snake()
    
    segmenta_position=[(0,0),(-20,0),(-40,0)]
    segments=[]
    def add_segment(self,pos):
        new_segment=self.Turtle(shape='square')
        new_segment.color('white')
        new_segment.pu()
        new_segment.goto(pos)
        self.segments.append(new_segment)    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.creat_snake()
    def creat_snake(self):
        for _ in self.segmenta_position:

            self.add_segment(_)
    
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x=self.segments[seg_num-1].xcor()
            y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading() !=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() !=90:
            self.segments[0].setheading(-90)
    def left(self):
        if self.segments[0].heading() !=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() !=180:
            self.segments[0].setheading(0)