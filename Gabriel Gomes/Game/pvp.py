import pygame

pygame.init()

jan = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Futeball Pong")
win= pygame.image.load("assets/win.png")

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

field = pygame.image.load("assets/field.png")

p1 = pygame.image.load("assets/player1.png")
p1_y = 310
p1_moveup = False
p1_movedown = False

p2 = pygame.image.load("assets/player2.png")
p2_y = 310
p2_moveup = False
p2_movedown = False

bola = pygame.image.load("assets/ball.png")
bola_x = 617
bola_y = 337
bola_dir = -3
bola_dir_y = 1


def move_player():
    global p1_y

    if p1_moveup:
        p1_y -= 5
    else:
        p1_y += 0

    if p1_movedown:
        p1_y += 5
    else:
        p1_y += 0

    if p1_y <= 0:
        p1_y = 0
    elif p1_y >= 575:
        p1_y = 575


def move_player2():
    global p2_y
    if p2_moveup:
        p2_y -= 5
    else:
        p2_y += 0

    if p2_movedown:
        p2_y += 5
    else:
        p2_y += 0

    if p2_y <= 0:
        p2_y = 0
    elif p2_y >= 575:
        p2_y = 575


def move_bola():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    global score1
    global score2
    global score2_img
    global score1_img

    bola_x += bola_dir
    bola_y += bola_dir_y

    if bola_x < 120:
        if p1_y < bola_y + 23:
            if p1_y + 146 > bola_y:
                bola_dir *= -1

    if bola_x > 1100:
        if p2_y < bola_y + 23:
            if p2_y + 146 > bola_y:
                bola_dir *= -1

    if bola_y > 685:
        bola_dir_y *= -1
    elif bola_y <= 0:
        bola_dir_y *= -1

    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")

    elif bola_x > 1320:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")


def draw():
    if score1 or score2 <9:
        jan.blit(field, (0, 0))
        jan.blit(p1, (50, p1_y))
        jan.blit(p2, (1150, p2_y))
        jan.blit(bola, (bola_x, bola_y))
        jan.blit(score1_img, (500, 50))
        jan.blit(score2_img, (710, 50))
        move_player()
        move_player2()
        move_bola()
        
    else:
       jan.blit(win,(300,300))


loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                p1_moveup = True
            if events.key == pygame.K_s:
                p1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                p1_moveup = False
            if events.key == pygame.K_s:
                p1_movedown = False
                
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                p2_moveup = True
            if events.key == pygame.K_DOWN:
                p2_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                p2_moveup = False
            if events.key == pygame.K_DOWN:
                p2_movedown = False

    draw()
   
    pygame.display.update()



