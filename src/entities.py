import pygame, random, colors

pygame.mixer.init()
appleSound = pygame.mixer.Sound("C:\casteluc\Coding\snakeGame\sounds\soundApple.wav")

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

screenSize = WIDTH, HEIGHT = 560, 660

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.body = [(260, 320), (280, 320), (300, 320), (320, 320)]
        self.size = 20
        self.bodySurface = pygame.Surface((self.size, self.size))
        self.bodySurface.fill(colors.GREEN)
        self.direction = LEFT
        self.score = 0
    
    def draw(self):
        for pos in self.body:
            self.screen.blit(self.bodySurface, pos)
    
    def move(self):
        for e in range(len(self.body) - 1, 0, -1):
            self.body[e] = (self.body[e - 1][0], self.body[e - 1][1])
        
        if self.direction == UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - self.size)
        if self.direction == DOWN:
            self.body[0] = (self.body[0][0], self.body[0][1] + self.size)
        if self.direction == RIGHT:
            self.body[0] = (self.body[0][0] + self.size, self.body[0][1])
        if self.direction == LEFT:
            self.body[0] = (self.body[0][0] - self.size, self.body[0][1])
    
    def selfCollided(self):
        for e in range(1, len(self.body)):
            if self.body[0] == self.body[e]:
                return True
        return False

    def checkBorderCollision(self):
        if self.body[0][0] >= WIDTH:
            self.body[0] = (0, self.body[0][1])
        elif self.body[0][0] < 0:
            self.body[0] = (WIDTH - self.size, self.body[0][1])
        elif self.body[0][1] >= HEIGHT:
            self.body[0] = (self.body[0][0], 20)
        elif self.body[0][1] < 20:
            self.body[0] = (self.body[0][0], HEIGHT - self.size)

    def checkAppleCollision(self, apple):
        if self.body[0] == apple.pos:
            appleSound.play()
            self.body.append(self.body[len(self.body) - 1])
            apple.updatePos(self)
            self.score += 10


class Apple():
    def __init__(self, screen):
        self.pos = (random.randrange(0, WIDTH - 20, 20), random.randrange(20, 300, 20))
        self.size = 20
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(colors.RED)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.surface, self.pos)

    def updatePos(self, snake):
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
        