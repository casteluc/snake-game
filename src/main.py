import pygame, sys, entities
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

WHITE, BLACK, GREEN, RED  = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0) 
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

screenSize = WIDTH, HEIGHT = 560, 660
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Snake Game")
snake = entities.Snake(screen)

def drawGrid():
    for e in range(20, WIDTH, 20):
        pygame.draw.line(screen, (20, 20, 20), (e, 0), (e, HEIGHT))
    for e in range(20, HEIGHT, 20):
        pygame.draw.line(screen, (20, 20, 20), (0, e), (WIDTH, e))

def renderScreen():
    screen.fill((0, 0, 0))
    snake.draw()
    drawGrid()
    pygame.display.update()
    
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and snake.direction != DOWN:
                snake.direction = UP
            
            if event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
                
            if event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT
                
            if event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT

    snake.move()

    renderScreen()
