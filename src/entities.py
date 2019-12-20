import pygame, random

WHITE, BLACK, GREEN, RED  = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0) 
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.body = [(260, 320), (280, 320), (300, 320), (320, 320)]
        self.size = 20
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(GREEN)
        self.direction = LEFT
    
    def draw(self):
        for pos in self.body:
            self.screen.blit(self.surface, pos)
    
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

# class Apple():
#     def __init__(self):
#         self.size = 20
#         self.pos = (random.randrange(0, )