import sys, pygame, math, random
from PlayerPaddle import *
from Ball import *
from Score import *
from Menu import *
pygame.init()

clock = pygame.time.Clock()

width = 900
height = 700
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

mode = "start"

while True:
    while mode == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "pvp"
                if event.key == pygame.K_2:
                    mode = "practice"
                    
        bg = pygame.image.load("Pics/menubackground.png")
        bgrect = bg.get_rect(center = [width/2,height/2])
        option = pygame.image.load("Pics/Gamemodeimageoptions.png")
        optionrect = option.get_rect(center = [width/2, 3*height/4])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(option, optionrect)
        pygame.display.flip()
        clock.tick(60)
        
    balls = []
    ballTimer = 0
    ballTimerMax = 5 * 60

    player = PlayerPaddle( ["Pics/Player/player.png"], [10,10], [10, height/2])
    player2 = PlayerPaddle( ["Pics/Player/player2.png"], [10,10], [890, height/2])

    scoreP1 = Score([300, 350])
    scoreP2 = Score([600, 350])

    endScore = 15
    lastScore = random.randint(1,2)
    beginningScore = 0    
    while mode == "pvp":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                elif event.key == pygame.K_s:
                    player.go("down")

                elif event.key == pygame.K_UP:
                    player2.go("up")
                elif event.key == pygame.K_DOWN:
                    player2.go("down")
               
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                elif event.key == pygame.K_s:
                    player.go("stop down")
                
                elif event.key == pygame.K_UP:
                    player2.go("stop up")
                elif event.key == pygame.K_DOWN:
                    player2.go("stop down")
                    
        ballTimer += 1
        if ballTimer >= ballTimerMax:
            ballTimer = 0
            if len(balls) < 3:
                d = random.randint(1,2)
                if lastScore == 1:
                    if d == 1:
                        ballSpeed = [random.randint(-8,-7), random.randint(-8,-7)]
                    else:
                        ballSpeed = [random.randint(-8,-7), random.randint(7,8)]
                else:
                    if d == 1:
                        ballSpeed = [random.randint(7,8), random.randint(-8,-7)]
                    else:
                        ballSpeed = [random.randint(7,8), random.randint(7,8)]
                balls += [Ball(["Pics/Ball/BlackBall.png",
                                "Pics/Ball/BlackBall1.png",
                                "Pics/Ball/BlackBall2.png",
                                "Pics/Ball/BlackBall3.png"],
                                ballSpeed,
                               [435,338])]
                    #print len(balls), clock.get_fps()
            
        player.update(size)
        player2.update(size)
        scoreP1.update()
        scoreP2.update()
            
        for ball in balls:
            ball.update(size)
            if ball.collideScreen(size) == "right":
                scoreP1.increase(1)
                lastScore = 1
            elif ball.collideScreen(size) == "left":
                scoreP2.increase(1)
                lastScore = 2
            
        for first in balls:
            first.collidePaddle(player)
            first.collidePaddle(player2)
            for second in balls:
                if first != second:
                    first.collideBall(second)
                elif second != first:
                    second.collideBall(first)
        
        for ball in balls:
            if not ball.living:
                balls.remove(ball)
            
        if scoreP1.score >= endScore and scoreP2.score <= endScore:
            mode = "player 1 win"
        if scoreP2.score >= endScore and scoreP1.score <= endScore:
            mode = "player 2 win"
        
        bgColor = r,b,g
        screen.fill(bgColor)
        screen.blit(scoreP1.image, scoreP1.rect)
        screen.blit(scoreP2.image, scoreP2.rect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        screen.blit(player.image, player.rect)
        screen.blit(player2.image, player2.rect)

        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
    
    balls = []
    ballTimer = 0
    ballTimerMax = 3 * 60

    player = PlayerPaddle( ["Pics/Player/player.png"], [10,10], [10, height/2])
    pracwall = PlayerPaddle( ["Pics/Player/largepaddle.png"], [10,10], [890, height/2])
    
    scoreP1 = Score([300, 350])

    endScore = 10000
    lastScore = random.randint(1,2)
    beginningScore = 0    
    while mode == "practice":
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
            
        if scoreP1.score >= endScore:
            mode = "practice lose"
            
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
        
            
        
    while mode == "player 1 win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "start"
                    
        playAgain = pygame.image.load("Pics/Player/playagain.png")
        playAgainRect = playAgain.get_rect(center = [width/2,3*height/4])
        bg = pygame.image.load("Pics/Player/player1wins.png")
        bgrect = bg.get_rect(center = [width/2,height/3])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(playAgain, playAgainRect)
        pygame.display.flip()
        clock.tick(60)
        
            
        
    while mode == "player 2 win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "start"
                
        playAgain = pygame.image.load("Pics/Player/playagain.png")
        playAgainRect = playAgain.get_rect(center = [width/2,3*height/4])
        bg = pygame.image.load("Pics/Player/player2wins.png")
        bgrect = bg.get_rect(center = [width/2,height/3])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(playAgain, playAgainRect)
        pygame.display.flip()
        clock.tick(60)

    while mode == "practice lose":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "start"
                    
        playAgain = pygame.image.load("Pics/Player/playagain.png")
        playAgainRect = playAgain.get_rect(center = [width/2,3*height/4])
        bg = pygame.image.load("Pics/Player/practicelose.png")
        bgrect = bg.get_rect(center = [width/2,height/3])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(playAgain, playAgainRect)
        pygame.display.flip()
        clock.tick(60)
