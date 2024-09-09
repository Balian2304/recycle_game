import pygame
import random
import time

WIDTH = 1000
HEIGHT = 1000
TITLE = "RECYCLE GAME"

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
score = 0
font = pygame.font.SysFont("Arial", 36)
background = pygame.image.load("bg.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  
bag_img = pygame.image.load("bag.png").convert_alpha()
bag_img = pygame.transform.scale(bag_img, (50, 50)) 
paperbag_img = pygame.image.load("paperbag.png").convert_alpha()
paperbag_img = pygame.transform.scale(paperbag_img, (50, 50)) 
box_img = pygame.image.load("box.png").convert_alpha()
box_img = pygame.transform.scale(box_img, (50, 50))  
pencil_img = pygame.image.load("pencil.png").convert_alpha()
pencil_img = pygame.transform.scale(pencil_img, (50, 50)) 
bin_img = pygame.image.load("bin.png").convert_alpha()
bin_img = pygame.transform.scale(bin_img, (50, 50))  

class Bin(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 4
        elif keys[pygame.K_UP]:
            self.rect.y -= 4
        elif keys[pygame.K_DOWN]:
            self.rect.y += 4

class Bag(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Paperbag(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Box(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pencil(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
bingroup = pygame.sprite.Group()
non_recycleable = pygame.sprite.Group()
recycleable = pygame.sprite.Group()
bin_obj = Bin(bin_img, 100, 100)
bingroup.add(bin_obj)

for i in range(15):
    bag = Bag(bag_img,random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50))
    non_recycleable.add(bag)
for i in range(12):
    paperbag = Paperbag(paperbag_img,random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50))
    recycleable.add(paperbag)
for i in range(11):
    box = Box(box_img,random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50))
    recycleable.add(box)
for i in range(14):
    pencil = Pencil(pencil_img,random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50))
    recycleable.add(pencil)
starttime = time.time()
totaltime = 0
run = True
while run:
    totaltime = time.time() - starttime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.sprite.groupcollide(bingroup,recycleable,False,True):
        score += 1
    if pygame.sprite.groupcollide(bingroup,non_recycleable,False,True): 
        score -= 1
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(score_text,(100,50))
    timetext = font.render("Time: " + str(30 - round(totaltime,0)),True,(255,255,255))
    screen.blit(timetext,(800,50))
    if score >= 25:
        wintext = font.render("YOU WON!",True,(255,255,255))
        screen.blit(background, (0,0))
        screen.blit(wintext,(500,500))
        pygame.display.update()
        time.sleep(5)
        run = False
    if totaltime >= 30:
        lose = font.render("YOU LOST :(",True,(255,255,255))
        screen.blit(background, (0,0))
        screen.blit(lose,(500,500))
        pygame.display.update()
        time.sleep(5)
        run = False
    bingroup.draw(screen)
    non_recycleable.draw(screen)    
    recycleable.draw(screen)
    pygame.display.flip()
    bin_obj.move()
pygame.quit()
