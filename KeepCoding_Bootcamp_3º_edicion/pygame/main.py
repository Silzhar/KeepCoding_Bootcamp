import pygame as pg
from pygame.locals import *
import sys
import random

_fps = 60

class Ball(pg.Surface):
    x = 0
    y = 0
    dirx = 1
    diry = 1
    color = (255, 255, 255)
    velocidad = 5

    def __init__(self):
        pg.Surface.__init__(self, (16,16))
        self.fill(self.color)

    def setColor(self, color):
        self.color = color
        self.fill(self.color)

    def avanza(self):
        if self.x >= 800:
            self.dirx = -self.velocidad
        if self.x <= 0:
            self.dirx = self.velocidad
        if self.y >= 600:
            self.diry = -self.velocidad
        if self.y <= 0:
            self.diry = self.velocidad

        self.x += self.dirx
        self.y += self.diry

    def comprobarChoque(self, candidata):

       if (candidata.x >= self.x and candidata.x <= self.x+16 or \
          candidata.x+16 >= self.x and candidata.x+16 <= self.x+16) and \
          (candidata.y >= self.y and candidata.y <= self.y+16 or \
           candidata.y+16 >= self.y and candidata.y+16 <= self.y+16):

           self.dirx = self.dirx * -1
           self.x += self.dirx



class Game:
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display
        self.screen = self.display.set_mode(self.size)
        self.screen.fill((60, 60, 60))
        self.display.set_caption('Mi juego')

        self.balls = []
        


        self.ball1 = Ball()
        self.ball1.setColor((255, 0, 0))
        self.ball1.x = random.randrange(800)
        self.ball1.y = random.randrange(600)
        self.ball1.velocidad = random.randrange(2, 9)

        self.ball2 = Ball()
        self.ball2.setColor((255, 255, 0))
        self.ball2.x = random.randrange(800)
        self.ball2.y = random.randrange(600)
        self.ball2.velocidad = random.randrange(2, 9)


        '''
        for i in range(5, 15):
            b = Ball()
            b.setColor((random.randrange(256), random.randrange(256), random.randrange(256)))
            b.x = random.randrange(800)
            b.y = random.randrange(600)
            b.velocidad = random.randrange(10)
            
            self.balls.append(b)   '''

        '''
        self.ball = Ball()
        self.ball1 = Ball()
        self.ball1.setcolor = ((255,0,0))
        self.ball1.x = 392
        self.ball1.y = 292
        self.ball1.velocidad = 10   '''


    def start(self):
        while True:
            self.clock.tick(_fps)

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            self.ball1.avanza()
            self.ball2.avanza()

            self.ball1.comprobarChoque(self.ball2)
            self.ball2.comprobarChoque(self.ball1)

        #    if self.ball1.comprobarChoque(self.ball2):
         #       print(" hay choque")

            self.screen.fill((60,60,60))

            self.screen.blit(self.ball1, (self.ball1.x , self.ball1.y))
            self.screen.blit(self.ball2, (self.ball2.x , self.ball2.y))
            '''
            #Modifica la posición de ball
            for ball in self.balls:
                ball.avanza()

            #Pintar los sprites en screen
            self.screen.fill((60,60,60))
            for i in range(5):
                self.screen.blit(self.balls[i],(self.balls[i].x,self.balls[i].y))

            for balls in self.balls:
                self.screen.blit(balls, (balls.x , balls.y))  '''

            self.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game(800, 600)
    game.start()
