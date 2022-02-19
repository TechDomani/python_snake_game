from food import Food

class Snake:   

    def __init__(self, width, height, size):
        self.width = width
        self.height = height        
        self.size = size
        self.x = self.width/2
        self.y = self.height/2
        self.change_x = 0
        self.change_y = 0
        self.increment = size
        self.speed = 5
        self.food = Food(width, height, size) 

    def reset(self):
        self.x = self.width/2
        self.y = self.height/2
        self.change_x = 0
        self.change_y = 0

    def setLeft(self):
        self.change_x = -1*self.increment
        self.change_y = 0

    def setRight(self):
        self.change_x = self.increment
        self.change_y = 0

    def setUp(self):
        self.change_y = -1*self.increment
        self.change_x = 0
    
    def setDown(self):
        self.change_y = self.increment
        self.change_x = 0

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def hasLost(self):
        return self.x > self.width or self.x < 0 or self.y > self.height or self.y < 0

    def hasEaten(self):
        if (self.x == self.food.x and self.y == self.food.y):
            self.food.updateFoodLocation()
            return True
        return False