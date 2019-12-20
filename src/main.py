import pygame, sys, entities, colors, time
from pygame.locals import *

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SINGLE, MULTI = 0, 1

pygame.init()
pygame.mixer.init()

# Loads the game over sound and starts the clock
gameOverSound = pygame.mixer.Sound("C:\casteluc\Coding\snakeGame\sounds\gameOver.wav")
clock = pygame.time.Clock()

# Sets the screen size and its caption
screenSize = WIDTH, HEIGHT = 560, 660
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Snake Game")
gamemode = SINGLE

# Creates the snakes initial bodies and inits the snake 1
snakeBody = [(260, 320), (280, 320), (300, 320), (320, 320)]
snakeBody2 = [(260, 360), (280, 360), (300, 360), (320, 360)]
snake = entities.Snake(snakeBody, colors.GREEN, screen)
snake2 = None

# Creates the apple, the list of snakes and the score set to 0
apple = entities.Apple(screen)
snakes = [snake]
score = 0

def gameOver():
    # Plays a game over sound and then waits 1 second ultil 
    # showing the game over messages 
    gameOverSound.play()
    time.sleep(1)

    # Loads the game over text
    overFont = pygame.font.Font("freesansbold.ttf", 72)
    overText = overFont.render("GAME OVER", True, (colors.WHITE)) 
    overTextRect = overText.get_rect()
    overTextRect.center = (WIDTH // 2, (HEIGHT // 2) - 70)
    
    # Loads the result font
    resultFont = pygame.font.Font("freesansbold.ttf", 30)
    
    # Defines which result will be shown according to if the game was single or multiplayer,
    # and to who won the game
    if gamemode == SINGLE:
        resultText = resultFont.render("Your score: %d" % score, True, colors.YELLOW)
    elif gamemode == MULTI:
        if len(snakes) > 0:
            if snakes[0].color == colors.BLUE:
                resultText = resultFont.render("The Blue Snake wins!", True, colors.YELLOW)
            else:
                resultText = resultFont.render("The Green Snake wins!", True, colors.YELLOW)
        else:
            resultText = resultFont.render("Both players lose", True, colors.YELLOW)
    
    resultTextRect = resultText.get_rect()
    resultTextRect.center = (WIDTH// 2, HEIGHT//2)
    
    # Blits all the game over texts on the screen
    screen.fill(colors.BLACK)
    screen.blit(overText, overTextRect)
    screen.blit(resultText, resultTextRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# Draw a gray grid in the whole screen
def drawGrid():
    for e in range(20, WIDTH, 20):
        pygame.draw.line(screen, colors.GRAY, (e, 0), (e, HEIGHT))
    for e in range(20, HEIGHT, 20):
        pygame.draw.line(screen, colors.GRAY, (0, e), (WIDTH, e))

# Draw the scoreboard on the top of the screen
def drawScore():
    pygame.draw.line(screen, colors.BLACK, (0, 0), (WIDTH, 0), 40)
    scoreFont = pygame.font.Font("freesansbold.ttf", 18)
    scoreText = scoreFont.render("Score: %d" % score, True, (255, 255, 255)) 
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (60, 10)

    screen.blit(scoreText, scoreTextRect)

# Calls all the functions needed to render the screen
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
    # Defines the game FPS (snake speed)
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        # Checks for entry to change the green direction
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and snake.direction != DOWN:
                snake.direction = UP
            if event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            if event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT
            if event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            
            # By pressing space, a new snake is created and the game becomes multiplayer
            if event.key == K_SPACE and snake2 == None:
                snake2 = entities.Snake(snakeBody2, colors.BLUE, screen)     
                snakes.append(snake2)  
                gamemode = MULTI 

            # Checks if there is more than 1 player and then checks for
            # entry to change the blue snake direction
            if gamemode == MULTI:
                if event.key == K_w and snake2.direction != DOWN:
                    snake2.direction = UP
                if event.key == K_s and snake2.direction != UP:
                    snake2.direction = DOWN
                if event.key == K_d and snake2.direction != LEFT:
                    snake2.direction = RIGHT
                if event.key == K_a and snake2.direction != RIGHT:
                    snake2.direction = LEFT
    
    # Calls all the functions needed to run the actual game:
    # first move the snakes, cheks for collision with the borders,
    # checks for collision with the apple (implements score if collided) and 
    # checks for collision with other snake (removes the snake, renders the
    # screen again and calls game over if collided)
    for s in snakes:
        s.move()
        s.checkBorderCollision()
        if s.checkAppleCollision(apple, snakes):
            score += 10
        if s.collidedSnake(snakes):
            snakes.remove(s)
            if gamemode == MULTI:
                renderScreen()
            gameOver()

    renderScreen()