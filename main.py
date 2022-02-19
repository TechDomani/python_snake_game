import pygame
from snake import Snake

pygame.init()
width = 800
height = 600
snakeSize = 20
gameSnake = Snake(width, height, snakeSize)

white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake game')

blue=(0,0,255)
red=(255,0,0)
font_style = pygame.font.SysFont(None, 50)

def message(msg, color, w=0.4, h=0.5):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width*w, dis_height*h])

def game_loop():
    game_over = False
    while not game_over:     
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gameSnake.setLeft()
                if event.key == pygame.K_RIGHT:
                    gameSnake.setRight()
                if event.key == pygame.K_UP:
                    gameSnake.setUp()
                if event.key == pygame.K_DOWN:
                    gameSnake.setDown()
        gameSnake.move()
        dis.fill(white)
        pygame.draw.rect(dis,black,[gameSnake.x, gameSnake.y, gameSnake.size, gameSnake.size])
        pygame.draw.rect(dis,blue,[gameSnake.food.x, gameSnake.food.y, gameSnake.size, gameSnake.size])
        if (gameSnake.hasEaten()):
            print("Yummy")
        pygame.display.update()
        clock.tick(gameSnake.speed)

        while gameSnake.hasLost():
            message("You lost! Press Q-Quit or C-Play Again", red, 0.1, 0.4)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:                 
                    game_over=True
                    gameSnake.reset()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        gameSnake.reset()
                    elif event.key == pygame.K_c:
                        gameSnake.reset()
                        
game_loop()
pygame.quit()
quit()