import pygame, sys, entities, colors, time
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

screenSize = WIDTH, HEIGHT = 560, 660
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Snake Game")

snake = entities.Snake(screen)
apple = entities.Apple(screen)

def gameOver():
    time.sleep(1)
    overFont = pygame.font.Font("freesansbold.ttf", 72)
    overText = overFont.render("GAME OVER", True, (255, 255, 255)) 
    overTextRect = overText.get_rect()
    overTextRect.center = (WIDTH // 2, HEIGHT // 2)
    
    screen.fill(colors.BLACK)
    screen.blit(overText, overTextRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def drawGrid():
    for e in range(20, WIDTH, 20):
        pygame.draw.line(screen, colors.GRAY, (e, 0), (e, HEIGHT))
    for e in range(20, HEIGHT, 20):
        pygame.draw.line(screen, colors.GRAY, (0, e), (WIDTH, e))

def drawScore():
    pygame.draw.line(screen, colors.BLACK, (0, 0), (WIDTH, 0), 40)
    scoreFont = pygame.font.Font("freesansbold.ttf", 18)
    scoreText = scoreFont.render("Score: %d" % snake.score, True, (255, 255, 255)) 
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (60, 10)

    screen.blit(scoreText, scoreTextRect)

def renderScreen():
    screen.fill(colors.BLACK)
    snake.draw()
    apple.draw()
    drawGrid()
    drawScore()
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
    snake.checkBorderCollision()
    snake.checkAppleCollision(apple)
    if snake.selfCollided():
        gameOver()

    renderScreen()