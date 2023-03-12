# Розроби свою гру в цьому файлі!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed=player_x_speed
        self.y_speed=player_y_speed

    def update(self):
        if hero.rect.x <= win_width-80 and hero.x_speed > 0 or hero.rect.x >= 0 and hero.x_speed <0:
            self.rect.x += self.x_speed
        platforms_touched=sprite.spritecollide(self,barriers,False)
        if self.x_speed>0:
            for p in platforms_touched:
                self.rect.right=min(self.rect.right, p.rect.left)
        elif self.x_speed<0:
            for p in platforms_touched:
                self.rect.left=max(self.rect.left, p.rect.right)
        if hero.rect.y <= win_height-80 and hero.y_speed > 0 or hero.rect.y >= 0 and hero.y_speed <0:
            self.rect.y += self.y_speed
        platforms_touched=sprite.spritecollide(self,barriers,False)
        if self.y_speed >0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                self.rect.bottom=min(self.rect.bottom,p.rect.top)    
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top=max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet=Bullet('bamm.png',self.rect.centerx,self.rect.top,15,20,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed, start_x1, start_x2):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)        
        self.speed=player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2
    def update(self):
        if self.rect.x <= self.start_x1:
            self.side='right'
        if self.rect.x >= win_width - self.start_x2:
            self.side='left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed=player_speed

    def update(self):
        self.rect.x +=self.speed
        if self.rect.x > win_width+10:
            self.kill()

                                        
win_width = 700
win_height= 500
display.set_caption('Лабіринт')
window=display.set_mode((win_width,win_height))  
back=transform.scale(image.load('fon2.jpg'), (700, 500))  

barriers=sprite.Group()

bullets=sprite.Group()

monster=sprite.Group()

w1=GameSprite('stena11.png',0,350,250,50)
w2=GameSprite('stena12.png',250,100,50,300)
w3=GameSprite('stena111.jpg',440,0,50,200)
w4=GameSprite('stena12.jpg',490,80,110,50)
w5=GameSprite('stena11.jpg',100,0,50,200)
w6=GameSprite('stena12.jpg',400,350,300,55)
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)

hero= Player('ghosttt2.png',5,win_height - 490,80,80,0,0)
enemy=Enemy('nindz.png',win_width - 80,210,80,80,5, 310, 85) ########
enemy2=Enemy('nindz.png',win_width - 690,250,80,80,5, 0,540 ) #########
enemy3=Enemy('nindz.png',win_width - 400,410,80,80,5,80,70)
final_sprite=GameSprite('sundukk.png',win_width - 690,win_height-80,80,80)

monster.add(enemy)
monster.add(enemy2)
monster.add(enemy3)
finish=False
false=False
run=True
while run:
    
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key== K_LEFT:
                hero.x_speed = -8
            elif i.key== K_RIGHT:
                hero.x_speed = 8
            elif i.key == K_UP:
                hero.y_speed = -8
            elif i.key == K_DOWN:
                hero.y_speed = 8
            elif i.key == K_SPACE:
                hero.fire()      
        elif i.type == KEYUP:
            if i.key== K_LEFT:
                hero.x_speed = 0
            elif i.key== K_RIGHT:
                hero.x_speed = 0
            elif i.key == K_UP:
                hero.y_speed = 0
            elif i.key == K_DOWN:
                hero.y_speed = 0

    if not finish:
        window.blit(back,(0,0))
        barriers.draw(window)
        final_sprite.reset()
        hero.reset()
        hero.update()
        bullets.update()
        bullets.draw(window)

        sprite.groupcollide(monster,bullets, True,True)
        monster.update()
        monster.draw(window)
        sprite.groupcollide(bullets,barriers,True,False)

        if sprite.spritecollide(hero,monster,False):
            finish=True
            img=image.load('gameoover.jpg')
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))

        if sprite.collide_rect(hero,final_sprite):
            finish=True
            img=image.load('win.jpg')             
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))


        time.delay(50)
        display.update()            



