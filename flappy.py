import pygame
import random
import time
while True:
        clock=pygame.time.Clock()
        pygame.init()
        screen = pygame.display.set_mode((700,700))
        done = False
        dead = False
        birdTexture=pygame.image.load("./images/bird.png")
        pygame.mixer.music.load("./sounds/background.mp3")
        pygame.mixer.music.play(-1)
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Flappy Bird", True, (255,255,0))
        buttonsFont=pygame.font.SysFont("comicsansms",30)
        startText=buttonsFont.render("Start!",True,(0,0,0))
        exitText=buttonsFont.render("Exit!",True,(0,0,0))
        intro =True
        class bird():
                def __init__(self):
                        self.bird_x=60
                        self.bird_y=350
        class pipe():
                def __init__(self):
                        self.pipe1_y=0
                        self.pipe_x=400
                        self.pipe1_height=random.randint(150,500)
                        self.width=50
                        self.pipe2_y=self.pipe1_height+150
                        self.pipe2_height=700-self.pipe2_y
        class pipe2():
                def __init__(self):
                        self.pipe1_y=0
                        self.pipe_x=700
                        self.pipe1_height=random.randint(150,500)
                        self.width=50
                        self.pipe2_y=self.pipe1_height+150
                        self.pipe2_height=700-self.pipe2_y
        bird=bird()
        pipeArray=[]
        pipeArray.append(pipe())
        pipeArray.append(pipe2())
        gravity=2
        speed=1
        color=(0,255,0)
        result=0
        test=True
        test2=True
        closeGame=0
        def check_collision_top(pipe,bird):
                if not pipe.pipe_x>bird.bird_x+60:
                        if not pipe.pipe_x+pipe.width<bird.bird_x:
                                if not pipe.pipe1_y>bird.bird_y+60:
                                        if pipe.pipe1_height>bird.bird_y:
                                                return True
        def check_collision_bottom(pipe,bird):
                        if not pipe.pipe_x>bird.bird_x+60:
                                if not pipe.pipe_x+pipe.width<bird.bird_x:
                                        if not pipe.pipe2_y>bird.bird_y+60:
                                                if pipe.pipe2_y<bird.bird_y:
                                                        return True
        def check_in(pipe,bird):
                if bird.bird_x>pipe.pipe_x:
                        return True
        while intro:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:          
                                done = True
                click = pygame.mouse.get_pressed()
                mouse=pygame.mouse.get_pos()
                screen.fill((135,206,250))
                if ((100<mouse[0]<250)&(500<mouse[1]<540)):
                       pygame.draw.rect(screen,(0,255,0),(100,500,150,40))
                       pygame.draw.rect(screen,(200,0,0),(450,500,150,40))
                       if click[0] == 1:
                            intro=False  
                elif((450<mouse[0]<600)&(500<mouse[1]<540)):
                        pygame.draw.rect(screen,(0,200,0),(100,500,150,40))
                        pygame.draw.rect(screen,(255,0,0),(450,500,150,40))
                        if click[0] == 1:
                                quit()
                else:
                        pygame.draw.rect(screen,(0,200,0),(100,500,150,40))
                        pygame.draw.rect(screen,(200,0,0),(450,500,150,40))


                screen.blit(startText,((100+150/2)-45,(500+40/2)-20))
                screen.blit(exitText,((450+150/2)-35,(500+40/2)-20))  
                screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
                pygame.display.flip()
                clock.tick(10)
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:          
                                done = True
                                quit()
                        pressed=pygame.key.get_pressed()
                        if pressed[pygame.K_SPACE]:
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/sfx_wing.wav"))
                                bird.bird_y -= 50
                                gravity=2
                if(check_collision_top(pipeArray[0],bird)or(check_collision_top(pipeArray[1],bird))or(check_collision_bottom(pipeArray[0],bird))or(check_collision_bottom(pipeArray[1],bird))):
                        dead = True
                if(test):
                        if(check_in(pipeArray[0],bird)):
                                result+=1
                                test=False
                if(test2):
                        if(check_in(pipeArray[1],bird)):
                                result+=1
                                test2=False
                screen.fill((135,206,250))
                pygame.draw.rect(screen,color,pygame.Rect(pipeArray[0].pipe_x,pipeArray[0].pipe1_y,pipeArray[0].width,pipeArray[0].pipe1_height))
                pygame.draw.rect(screen,color,pygame.Rect(pipeArray[0].pipe_x,pipeArray[0].pipe2_y,pipeArray[0].width,pipeArray[0].pipe2_height))
                pygame.draw.rect(screen,color,pygame.Rect(pipeArray[1].pipe_x,pipeArray[1].pipe1_y,pipeArray[1].width,pipeArray[1].pipe1_height))
                pygame.draw.rect(screen,color,pygame.Rect(pipeArray[1].pipe_x,pipeArray[1].pipe2_y,pipeArray[1].width,pipeArray[1].pipe2_height))
                if pipeArray[1].pipe_x<-50:
                        pipeArray.clear()
                        pipeArray.append(pipe())
                        pipeArray.append(pipe2())
                        test=True
                        test2=True
                ##pygame.draw.rect(screen,(255,255,0),pygame.Rect(bird_x,bird_y,30,30))
                if not dead:
                        gravity+=0.05
                        bird.bird_y+=gravity
                        while speed<5:
                                speed+=0.00001
                        pipeArray[0].pipe_x-=speed
                        pipeArray[1].pipe_x-=speed
                        font=pygame.font.SysFont("comicsansms",30)
                        text=font.render(str(result),True,(255,255,255))
                        screen.blit(birdTexture,(bird.bird_x,bird.bird_y))
                        screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
                else:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/sfx_die.wav"))
                        birdTexture=pygame.image.load("./images/dead_bird.png")
                        screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
                        bird.bird_y+=5
                        screen.blit(birdTexture,(bird.bird_x,bird.bird_y))
                        closeGame+=1
                        text=font.render(str(result),True,(255,255,255))
                        screen.blit(birdTexture,(bird.bird_x,bird.bird_y))
                        screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
                        if closeGame==50:done=True
                        
                pygame.display.flip()
                clock.tick(60)
