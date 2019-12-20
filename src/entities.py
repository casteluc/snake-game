import pygame, random, colors

pygame.mixer.init()
appleSound = pygame.mixer.Sound("C:\casteluc\Coding\snakeGame\sounds\soundApple.wav")

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

screenSize = WIDTH, HEIGHT = 560, 660

# Defines a snake which has as attributes:
# the screen where it'll be displayed, the coordenates of its initial body,
# its size, its body surface filled with green or blue (depending of the player),
# the direction its going and its color in a dedicated variable
class Snake():
    def __init__(self, body, color, screen):
        self.screen = screen
        self.body = body
        self.size = 20
        self.bodySurface = pygame.Surface((self.size, self.size))
        self.bodySurface.fill(color)
        self.direction = LEFT
        self.color = color
    
    # Blits the whole snake on the screen
    def draw(self):
        for pos in self.body:
            self.screen.blit(self.bodySurface, pos)
    
    # Moves the snake through the screen
    def move(self):
        # Moving the body (except the head)
        for e in range(len(self.body) - 1, 0, -1):
            self.body[e] = (self.body[e - 1][0], self.body[e - 1][1])
        
        # Moving the head in the current direction (the rest of the body
        # follows the head movements)
        if self.direction == UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - self.size)
        if self.direction == DOWN:
            self.body[0] = (self.body[0][0], self.body[0][1] + self.size)
        if self.direction == RIGHT:
            self.body[0] = (self.body[0][0] + self.size, self.body[0][1])
        if self.direction == LEFT:
            self.body[0] = (self.body[0][0] - self.size, self.body[0][1])
    
    # Checks if the snake has collided with itself or with another snake,
    # using a list of snakes given by the main file
    def collidedSnake(self, snakes):
        for s in snakes:
            # checking for self collision
            if self == s:
                for e in range(1, len(s.body)):
                    if self.body[0] == s.body[e]:
                        return True
            # checking for collision with other snake
            else:
                for e in range(0, len(s.body)):
                    if self.body[0] == s.body[e]:
                        return True
        return False

    # Checks if the snake has hit a screen border, if so, the snake is teleported
    # to the other side of the screen
    def checkBorderCollision(self):
        if self.body[0][0] >= WIDTH:
            self.body[0] = (0, self.body[0][1])
        elif self.body[0][0] < 0:
            self.body[0] = (WIDTH - self.size, self.body[0][1])
        elif self.body[0][1] >= HEIGHT:
            self.body[0] = (self.body[0][0], 20)
        elif self.body[0][1] < 20:
            self.body[0] = (self.body[0][0], HEIGHT - self.size)

    # Checks if the snake has hit an apple, playing a sound and returning 
    # True or False for the score implementation
    def checkAppleCollision(self, apple, snakes):
        if self.body[0] == apple.pos:
            appleSound.play()
            self.body.append(self.body[len(self.body) - 1])
            apple.updatePos(snakes)
            return True
        return False

# Defines an apple which has as attributes:
# the screen where it'll be displayed, its initial position (which can be only
# in the firs half of the screen to avoid apple generating over the snake), its
# size, and its surface filled with red
class Apple():
    def __init__(self, screen):
        self.pos = (random.randrange(0, WIDTH - 20, 20), random.randrange(20, 300, 20))
        self.size = 20
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(colors.RED)
        self.screen = screen

    # Blits the apple on the screen
    def draw(self):
        self.screen.blit(self.surface, self.pos)

    # Updates the apple position, this algorithm checks if the new position is
    # available (without any snakes). This funtion is only used inside the Snake class
    def updatePos(self, snakes):
        for snake in snakes:
            posIsEqual = False
            self.pos = (random.randrange(0, WIDTH - 20, 20), random.randrange(20, HEIGHT - 20, 20))
            for snakePos in range(len(snake.body)):
                if self.pos == snakePos:
                    posIsEqual = True
            
            while posIsEqual:
                self.pos = (random.randrange(0, WIDTH - 20, 20), random.randrange(20, HEIGHT - 20, 20))
                for snakePos in range(len(snake.body)):
                    if self.pos == snake[snakePos]:
                        posIsEqual = True
                    else:
                        posIsEqual = False