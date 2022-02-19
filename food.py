import random

class Food:
    def __init__(self, width, height, snakeSize):
       self.width = width
       self.height = height
       self.snakeSize = snakeSize
       self.updateFoodLocation()

    def updateFoodLocation(self):
        self.x = round(random.randrange(0, self.width - self.snakeSize) / self.snakeSize) * self.snakeSize
        self.y = round(random.randrange(0, self.height - self.snakeSize) /  self.snakeSize) * self.snakeSize