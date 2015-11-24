import sys, pygame, math
from PlayerPaddle import *
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 120,0,56

screen = pygame.display.set_mode(size)

player = PlayerPaddle( ["pRainbow.png"], [6,6], [width/2, height/2] )
#player2 = PlayerPaddle( [width/2, height/2], "pRainbow.png")

ball = Ball(["BlackBall.png"], [6,6], [300,400])

balls = []
ballSpawnTimer = 0
ballSpawnTimerMax = 1* 60


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")
           
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
        
        player.update(size)
        
        for ball in balls:
            ball.update(size)
        
        bgColor = r,b,g
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
