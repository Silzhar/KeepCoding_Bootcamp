import pygame as pg
from pygame.locals import *
import sys
import random

_fps = 60

def between(valor, liminf, limsup):
    return valor >= liminf and valor <= limsup 
    # es igual a return liminf <= valor <= limsup 

class Raquet(pg.Surface):
    x = 0
    y = 0
    w = 16  # ancho
    h = 96  # alto 
    color = (255, 255, 255)
    velocidad = 5
    diry = 1

    def __init__(self):
        pg.Surface.__init__(self, (self.w, self.h))
        self.fill(self.color)

    def setColor(self, color):
        self.color = color
        self.fill(self.color)

    def avanza(self):
        self.y += self.diry * self.velocidad

        if self.y <=0:
            self.y = 0
 
        if self.y >= 600 - self.h:
            self.y = 600 - self.h


class Ball(pg.Surface):
    x = 0
    y = 0
    w = 16
    h = 16
    color = (255, 255, 255)
    velocidad = 5
    dirx = 1
    diry = 1

    def __init__(self):
        pg.Surface.__init__(self, (self.w, self.h))
        self.fill(self.color)

    def setColor(self, color):
        self.color = color
        self.fill(self.color)

    def saque(self, ganador):
        self.x = 392
        self.y = 292
        self.diry = random.choice([-1,1])

        if ganador == 1:
            self.dirx = -1
        else:
            self.dirx = 1


    def avanza(self):
        if self.x >= 800:
            self.saque(1)
            return 2

        if self.x <= 0:
            self.saque(2)
            return 1

        if self.y >= 584:
            self.diry = -1
        if self.y <= 0:
            self.diry = 1

        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        return None


    def comprobarChoque(self, candidata):

        if (between(self.y, candidata.y, candidata.y+candidata.h) or between(self.y+self.h, candidata.y, candidata.y+candidata.h)) and \
           (between(self.x, candidata.x, candidata.x+candidata.w) or between(self.x+self.w, candidata.x, candidata.x+candidata.w)):
            self.dirx = self.dirx * -1
            self.x += self.dirx

        '''
        if (candidata.x >= self.x and candidata.x <= self.x+self.w or \
           candidata.x+candidata.w >= self.x and candidata.x+candidata.w <= self.x+self.w) and \
           (candidata.y >= self.y and candidata.y <= self.y+self.h or \
            candidata.y+candidata.h >= self.y and candidata.y+candidata.h <= self.y+self.h):

            self.dirx = self.dirx * -1
            self.x += self.dirx   '''


class Game:
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display
        self.screen = self.display.set_mode(self.size)
        self.screen.fill((60, 60, 60))
        self.display.set_caption('Mi juego')

        self.ball1 = Ball()
        self.ball1.setColor((255, 0, 0))
        self.ball1.x = random.randrange(800)
        self.ball1.y = random.randrange(600)
        self.ball1.velocidad = random.randrange(2, 9)

        self.player1 = Raquet()
        self.player1.x = 768
        self.player1.y = 252

        self.player2 = Raquet()
        self.player2.x = 16
        self.player2.y = 252

    def start(self):
        while True:
            self.clock.tick(_fps)

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.player1.diry = -1
                        self.player1.velocidad = 15
                        self.player1.avanza()

                    if event.key == K_DOWN:
                        self.player1.diry = 1
                        self.player1.velocidad = 15
                        self.player1.avanza()  

                    if event.key == K_q:
                        self.player2.diry = -1
                        self.player2.velocidad = 15
                        self.player2.avanza()

                    if event.key == K_a:
                        self.player2.diry = 1
                        self.player2.velocidad = 15
                        self.player2.avanza()


            keys_pressed = pg.key.get_pressed()
            if keys_pressed[K_UP]:
                self.player1.diry = -1
                if self.player1.velocidad < 15:
                    self.player1.velocidad += 1
                self.player1.avanza()
                                 
            if keys_pressed[K_DOWN]:
                self.player1.diry = 1
                if self.player1.velocidad < 15:
                    self.player1.velocidad += 1
                self.player1.avanza()

            if keys_pressed[K_q]:
                self.player2.diry = -1
                if self.player2.velocidad < 15:
                    self.player2.velocidad += 1
                self.player2.avanza()

            if keys_pressed[K_a]:
                self.player2.diry = 1
                if self.player2.velocidad < 15:
                    self.player2.velocidad += 1
                self.player2.avanza()

            #Modifica la posición de ball
            self.ball1.avanza()
            self.ball1.comprobarChoque(self.player1)
            self.ball1.comprobarChoque(self.player2)


            #Pintar los sprites en screen
            self.screen.fill((60,60,60))

            self.screen.blit(self.ball1, (self.ball1.x, self.ball1.y))
            self.screen.blit(self.player1, (self.player1.x, self.player1.y))
            self.screen.blit(self.player2, (self.player2.x, self.player2.y))

            self.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game(800, 600)
    game.start()



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
