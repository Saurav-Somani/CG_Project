from turtle import *

class Character:

    def __init__(self):
        self.t = Turtle()
        t = self.t
        t.pensize(3)
        t.speed(0)

    def point(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def left_eye(self, x, y):
        self.point(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.point(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.point(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def right_eye(self, x, y):
        self.point(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.point(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.point(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth(self, x, y):
        self.point(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()
        
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)

        self.point(x, y)
        t.seth(10)
        
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
        
        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)
        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

    def nose(self, x, y):
        self.point(x,y)
        t=self.t
        t.seth(8)
        t.fd(4)
        t.back(8)

    def draw_the_character(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        
        #Right cheek
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        #Right ear
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        #Upper head
        t.seth(150)
        t.circle(150, 70)

        #Left ear
        t.seth(140)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(310)
        t.circle(300, 33)

        #Left cheek
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        #Left hand
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        #Left part of body
        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        #Left leg
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        #Bottom part of body
        t.seth(330)
        t.circle(150, 60)

        #Right leg
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        #Right part of body
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 15)

        #Right hand
        t.seth(330)
        t.circle(300, 18)
        t.seth(100)
        t.circle(10, 70)
        t.seth(50)
        t.fd(13)
        t.seth(100)
        t.circle(10, 70)
        t.seth(40)
        t.fd(8)
        t.circle(10, 80)
        t.seth(200)
        t.fd(10)
        t.seth(70)
        t.circle(10, 80)
        t.seth(40)
        t.fd(10)
        t.seth(210)
        t.fd(7)
        t.seth(100)
        t.fd(10)
        t.seth(125)
        t.circle(500, 24.25)
        t.seth(210)
        t.end_fill()

        #Tail
        self.point(190, 145)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        #Rest of the details
        self.left_eye(-85, 90)
        self.right_eye(50, 110)
        self.nose(-17,94)
        self.mouth(-5, 25)
        t.hideturtle()

    def start(self):
        self.draw_the_character()


def main():
    screen = Screen()
    screen.setup(800,800)
    screen.bgcolor("light green")
    character = Character()
    character.start()


if __name__ == '__main__':
    main()