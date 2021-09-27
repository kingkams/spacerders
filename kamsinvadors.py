import pygame
import math
import random

from pygame import mixer

# 2 start pygame
pygame.init()

screen = pygame.display.set_mode((800, 700))
# back dis
background = pygame.image.load("kmc.jpg")
bulletImg = pygame.image.load("bullet.png")

#background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("kams stj space shooters,")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon((icon))
# player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 580
LEFT = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemy_x = []
enemy_y = []
num_of_alliens = 10
for a in range(num_of_alliens):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(50, 169))
    enemy_x.append(6)
    enemy_y.append(40)

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

text_x = 10
text_y = 10

Game_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    looser = Game_font.render("You Loose " + str(score_value), True, (0, 255, 255))
    screen.blit(looser, (203, 252))


bulletX = 0
bulletY = 580
bulletX_change = 0
bulletY_change = 14
bullet_state = "ready"


# blit means to draw
def player(x, y, ):
    screen.blit(playerImg, (x, y))


def enemy(x, y, a):
    screen.blit(enemyImg[a], (x, y,))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
numz = [1,5,8,9,7,1647,90]

def isCollision(enemyX, enemyY, bulletX, bulletY):
    collision_distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if collision_distance < 20:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # backdisp
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                LEFT = -8
            if event.key == pygame.K_RIGHT:
                LEFT = 8
            if event.key == pygame.K_a:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                LEFT = 0
    if bulletY <= 0:
        bulletY = 580
        bullet_state = "ready"

    playerX += LEFT
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 732:
        playerX = 732

    enemyX += enemy_x
    # collision

    for a in range(num_of_alliens):
        if enemyY[a] > 500:
            for d in range(num_of_alliens):
                enemyY[d] = 2000
            game_over_text()
            break
        enemyX[a] += enemy_x[a]
        if enemyX[a] <= 0:
            enemy_x[a] = 3
            enemyY[a] += enemy_y[a]
        elif enemyX[a] >= 732:
            enemy_x[a] = -3
            enemyY[a] += enemy_y[a]
        shoot = isCollision(enemyX[a], enemyY[a], bulletX, bulletY)
        if shoot:
            shoot = isCollision(enemyX[a], enemyY[a], bulletX, bulletY)
            explosion = mixer.Sound("explosion.wav")
            explosion.play()
            bulletY = 580
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[a] = random.randint(0, 730)
            enemyY[a] = random.randint(50, 169)

        enemy(enemyX[a], enemyY[a], a)
    show_score(text_x, text_y)
    player(playerX, playerY)
    pygame.display.update()
