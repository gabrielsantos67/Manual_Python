import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
window_title = pygame.display.set_caption("Futeball Pong")

#Criação do cenário
field= pygame.image.load('assets/field.png')
window.blit(field,(0,0))

#adicionar os players1
player1 = pygame.image.load("assets/player1.png")
window.blit(player1,(50,300))

#acicionando o plyer2
player2= pygame.image.load("assets/player2.png")
window.blit(player2,(1150, 310))

# ADICIONANDO a bola
ball = pygame.image.load("assets/ball.png")
window.blit(ball,(617, 337))
loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    #utilizado para atualizar simultaneamente
    pygame.display.update()
