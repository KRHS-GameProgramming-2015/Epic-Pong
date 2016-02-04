import sys, pygame, math, random
from PlayerPaddle import *
from Ball import *
from Score import*
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = 3 * 60

player = PlayerPaddle( ["Pics/Player/player.png"], [10,10], [10, height/2])
pracwall = PlayerPaddle( ["Pics/Player/largepaddle.png"], [10,10], [890, height/2])

scoreP1 = Score([300, 350])

endScore = 10
lastScore = random.randint(1,2)
beginningScore = 0

while True:
    while scoreP1.score < endScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                elif event.key == pygame.K_s:
                    player.go("down")
               
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                elif event.key == pygame.K_s:
                    player.go("stop down")
                    
        ballTimer += 1
        if ballTimer >= ballTimerMax:
            ballTimer = 0
            if len(balls) < 3:
                d = random.randint(1,2)
                if lastScore == 1:
                    if d == 1:
                        ballSpeed = [random.randint(-7,-6), random.randint(-7,-6)]
                    else:
                        ballSpeed = [random.randint(-7,-6), random.randint(6,7)]
                else:
                    if d == 1:
                        ballSpeed = [random.randint(6,7), random.randint(-7,-6)]
                    else:
                        ballSpeed = [random.randint(6,7), random.randint(6,7)]
                balls += [Ball(["Pics/Ball/BlackBall.png",
                                "Pics/Ball/BlackBall1.png",
                                "Pics/Ball/BlackBall2.png",
                                "Pics/Ball/BlackBall3.png"],
                                ballSpeed,
                               [435,338])]
                    #print len(balls), clock.get_fps()
            
        player.update(size)
        pracwall.update(size)
        scoreP1.update()
            
        for ball in balls:
            ball.update(size)
            print ball.rect.center
            if not ball.living:
                endScore = scoreP1.score
            if ball.collidePaddle(pracwall):
                scoreP1.increase(1)
                lastScore = 1
            
        for first in balls:
            first.collidePaddle(player)
            first.collidePaddle(pracwall)
            for second in balls:
                if first != second:
                    first.collideBall(second)
                elif second != first:
                    second.collideBall(first)
        
        for ball in balls:
            if not ball.living:
                balls.remove(ball)
            
        bgColor = r,b,g
        screen.fill(bgColor)
        screen.blit(scoreP1.image, scoreP1.rect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        screen.blit(player.image, player.rect)
        screen.blit(pracwall.image, pracwall.rect)

        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
        
        
        
    while scoreP1.score >= endScore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scoreP1.reset()
                    scoreP2.reset()
                    player.reset()
                    player2.reset()
                    
        playAgain = pygame.image.load("Pics/Player/playagain.png")
        playAgainRect = playAgain.get_rect(center = [width/2,3*height/4])
        bg = pygame.image.load("Pics/Player/player1wins.png")
        bgrect = bg.get_rect(center = [width/2,height/3])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(playAgain, playAgainRect)
        pygame.display.flip()
        clock.tick(60)
