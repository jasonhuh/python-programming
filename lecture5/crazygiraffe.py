import random

class Animal(object):
    def __init__(self):
        self.color = None
        self.position = {x:0, y:0}

    def move(self, x, y):
        self.x = x
        self.y = y
        print('move to x: {}, y: {}'.format(x, y))

class Giraffe(Animal):
    def __init__(self, name):
        self.name = name

    def left_foot_forward(self):
        print('left_foot_forward')

    def right_foot_forward(self):
        print('right_foot_forward')

    def left_foot_backward(self):
        print('left_foot_backward')

    def right_foot_backward(self):
        print('right_foot_backward')

class CrazyGiraffe(Giraffe):
    def __init__(self):
        self.facebook_followers = []

    def dance(self):
        steps = random.randint(3, 8)
        for _ in range(steps):
            move = random.randint(1, 4)
            if move == 1:
                self.left_foot_forward()
            elif move == 2:
                self.left_foot_backward()
            elif move == 3:
                self.right_foot_forward()
            elif move == 4:
                self.right_foot_backward()

    def backflip(self):
        print('Awesome backflip')

    def split(self):
        print('Crazy split')
