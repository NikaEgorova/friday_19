from pygame import *

#КЛАСИ
class GameSprite(sprite.Sprite):
    def __init__(self,width,height,x,y,img):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_pic(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,width,height,x,y,img,x_speed,y_speed):
        GameSprite.__init__(self,width,height,x,y,img)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(boar, walls,False)
        if self.x_speed > 0 :
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(boar, walls,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def dyno_update(self):
        platforms_touched = sprite.spritecollide(self, walls,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = -2
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 2
    def fire(self):
        acorn = Player(15,15,(self.rect.x + 37.5),(self.rect.y + 37.5),'acorn.png',0,0)
        acorns.add(acorn)
        acorn.draw_pic()
        if self.x_speed > 0:
            acorn.x_speed = 6
            acorn.update()
        elif self.x_speed < 0:
            acorn.x_speed = -6
            acorn.update()
        else:
            acorn.x_speed = 6
            acorn.update()

#ЗМІННІ
img =  transform.scale(image.load('back.png'),(700,500))
win = transform.scale(image.load('won.gif'),(700,500))
window = display.set_mode((701,501))
display.set_caption('Вікно')

wall = 'wall.jpg'
wall1 = GameSprite(25,75,75,425,wall)
wall2 = GameSprite(75,25,75,425,wall)
wall3 = GameSprite(525,25,75,300,wall)
wall4 = GameSprite(25,300,75,0,wall)
wall5 = GameSprite(25,75,275,325,wall)
wall6 = GameSprite(25,75,400,425,wall)
wall7 = GameSprite(200,25,400,400,wall)
wall8 = GameSprite(525,25,200,200,wall)
wall9 = GameSprite(25,125,200,100,wall)
wall10 = GameSprite(25,100,325,0,wall)
wall11 = GameSprite(25,50,450,150,wall)
wall12 = GameSprite(700,1,0,0,wall)
wall13 = GameSprite(1,500,-1,0,wall)
wall14 = GameSprite(700,1,0,501,wall)
wall15 = GameSprite(1,500,701,0,wall)

final = GameSprite(80,60,620,10,'flag1.png')
lose = transform.scale(image.load('you_died.png'),(700,500))

walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)
walls.add(wall8)
walls.add(wall9)
walls.add(wall10)
walls.add(wall11)
walls.add(wall12)
walls.add(wall13)
walls.add(wall14)
walls.add(wall15)

run = True
finish = False
dynos = sprite.Group()
acorns = sprite.Group()
boar = Player(75,75,0,425,'boar_007.png',0,0)
dyno = Player(55,55,615,240,'dinosaur.png',0,0)
dyno2 = Player(55,55,500,100,'dinosaur.png',0,0)
dynos.add(dyno)
dynos.add(dyno2)
acorn = Player(15,15,(boar.rect.x + 37.5),(boar.rect.y + 37.5),'acorn.png',0,0)
dyno.y_speed = 2
dyno2.y_speed = -2

while run:
    dyno2.update()
    dyno2.dyno_update()
    dyno.update()
    dyno.dyno_update()
    acorns.add(acorn)
    acorns.update()
    acorns.remove(acorn)
    time.delay(20)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                boar.y_speed = -5
                
            elif e.key == K_DOWN:
                boar.y_speed = 5
                
            elif e.key == K_LEFT:
                boar.x_speed = -5
                
            elif e.key == K_RIGHT:
                boar.x_speed = 5
            
            elif e.key == K_SPACE:
                boar.fire()

        elif e.type == KEYUP:
            if e.key == K_UP:
                boar.y_speed = 0
                
            elif e.key == K_DOWN:
                boar.y_speed = 0
                
            elif e.key == K_LEFT:
                boar.x_speed = 0
                
            elif e.key == K_RIGHT:
                boar.x_speed = 0
    if finish != True:                  
        window.blit(img,(0,0))
        walls.draw(window)
        boar.draw_pic()
        final.draw_pic()
        acorns.draw(window)
        sprite.groupcollide(dynos,acorns,True,True)
        dynos.update()
        dynos.draw(window)
        boar.update()  
        sprite.groupcollide(acorns,walls,True,False)
        if sprite.collide_rect(boar, final):
            finish = True
            window.blit(win,(0,0)) 
        if sprite.spritecollide(boar, dynos, False):
            finish = True
            window.blit(lose,(0,0))      
        display.update()