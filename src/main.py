import pygame, sys, entities, colors, time
from pygame.locals import *

pygame.init()
pygame.mixer.init()

gameOverSound = pygame.mixer.Sound("C:\casteluc\Coding\snakeGame\sounds\gameOver.wav")
clock = pygame.time.Clock()

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SINGLE, MULTI = 0, 1

screenSize = WIDTH, HEIGHT = 560, 660
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Snake Game")
gameType = SINGLE

snakeBody = [(260, 320), (280, 320), (300, 320), (320, 320)]
snakeBody2 = [(260, 360), (280, 360), (300, 360), (320, 360)]
snake = entities.Snake(snakeBody, colors.GREEN, screen)
snake2 = None
apple = entities.Apple(screen)

snakes = [snake]
score = 0

def gameOver():
    gameOverSound.play()
    time.sleep(1)
    overFont = pygame.font.Font("freesansbold.ttf", 72)
    overText = overFont.render("GAME OVER", True, (colors.WHITE)) 
    overTextRect = overText.get_rect()
    overTextRect.center = (WIDTH // 2, (HEIGHT // 2) - 70)
    
    resultFont = pygame.font.Font("freesansbold.ttf", 30)
    if gameType == SINGLE:
        resultText = resultFont.render("Your score: %d" % score, True, colors.YELLOW)
    elif gameType == MULTI:
        if len(snakes) > 0:
            if snakes[0].color == colors.BLUE:
                resultText = resultFont.render("The Blue Snake wins!", True, colors.YELLOW)
            else:
                resultText = resultFont.render("The Green Snake wins!", True, colors.YELLOW)
        else:
            resultText = resultFont.render("Both players lose", True, colors.YELLOW)
    
    resultTextRect = resultText.get_rect()
    resultTextRect.center = (WIDTH// 2, HEIGHT//2)
    
    screen.fill(colors.BLACK)
    screen.blit(overText, overTextRect)
    screen.blit(resultText, resultTextRect)

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
    scoreText = scoreFont.render("Score: %d" % score, True, (255, 255, 255)) 
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (60, 10)

    screen.blit(scoreText, scoreTextRect)

def renderScreen():
    screen.fill(colors.BLACK)
    for s in snakes:
        if s != None:
            s.draw()
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
            
            if event.key == K_SPACE and snake2 == None:
                snake2 = entities.Snake(snakeBody2, colors.BLUE, screen)     
                snakes.append(snake2)  
                gameType = MULTI             
            if snake2 != None:
                if event.key == K_w and snake2.direction != DOWN:
                    snake2.direction = UP
                if event.key == K_s and snake2.direction != UP:
                    snake2.direction = DOWN
                if event.key == K_d and snake2.direction != LEFT:
                    snake2.direction = RIGHT
                if event.key == K_a and snake2.direction != RIGHT:
                    snake2.direction = LEFT
            
    for s in snakes:
        s.move()
        s.checkBorderCollision()
        if s.checkAppleCollision(apple):
            score += 10
        if s.collidedSnake(snakes):
            snakes.remove(s)
            gameOver()

    renderScreen()