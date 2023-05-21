"""Por: Thiago Costa Thimoteo

Descrição: Este é um trabalho sobre a simulação das órbitas da Terra e da Lua usando círculos trigonométricos

"""
import pygame, math


class Corpo(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, largura=None, altura=None, angulo=0, raio=None):
        self.X = x
        self.Y = y
        self.Largura = largura
        self.Altura = altura
        assert 0 <= angulo < 360
        self.Angulo = angulo
        self.Raio = raio
        

    def atualizar(self):
        if self.Angulo < 360:
            self.Angulo += 1/12
        else:
            self.Angulo = 0
        
        self.X = math.cos(math.radians(self.Angulo)) * 100 + screen.get_width()/2
        self.Y = math.sin(math.radians(self.Angulo)) * 100 + screen.get_height()/2

class Satelite(Corpo):
    def __init__(self, x=None, y=None, largura=None, altura=None, angulo=0, raio=None):
        super().__init__(x, y, largura, altura, angulo, raio)
    
    def atualizar(self, XR, YR):
        if self.Angulo < 360:
            self.Angulo += 1
        else:
            self.Angulo = 0
        
        self.X = math.cos(math.radians(self.Angulo)) * 20 + XR
        self.Y = math.sin(math.radians(self.Angulo)) * 20 + YR


pygame.init()
pygame.display.set_caption('Órbitas')
screen = pygame.display.set_mode((1280/2, 720/2))
clock = pygame.time.Clock()
running = True
Terra = Corpo(raio=10, angulo=0)
Lua = Satelite(raio=4, angulo=0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    Terra.atualizar()
    Lua.atualizar(XR=Terra.X, YR=Terra.Y)
    pygame.draw.circle(screen, (255, 255, 0), (screen.get_width()/2, screen.get_height()/2), 25)
    pygame.draw.circle(screen, (0, 0, 255), (Terra.X, Terra.Y), Terra.Raio)
    pygame.draw.circle(screen, (255, 255, 255), (Lua.X, Lua.Y), Lua.Raio)

    pygame.display.flip()
    clock.tick(360)

pygame.quit()