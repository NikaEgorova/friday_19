from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, fimage, width, height, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(fimage), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        bg.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, p_image, width,height, x,y, player_x_speed,player_y_speed):
       GameSprite.__init__(self, p_image, width, height, x, y)
       self.x_speed = player_x_speed
       self.y_speed = player_y_speed

    def touch(self): 
       
        if cosmo.rect.x <= win_width-80 and cosmo.x_speed > 0 or cosmo.rect.x >= 0 and cosmo.x_speed < 0:
            self.rect.x += self.x_speed
           
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if cosmo.rect.y <= win_height-80 and cosmo.y_speed > 0 or cosmo.rect.y >= 0 and cosmo.y_speed < 0:
            self.rect.y += self.y_speed
        
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) 

    def fire(self):
        bullet = Bullet('lightning11.png', 45, 20, self.rect.right - 25, self.rect.centery - 16, 25)
        bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self, player_image, size_x, size_y, player_x, player_y, player_speed):
        GameSprite.__init__(self, player_image, size_x, size_y, player_x, player_y)
        self.speed = player_speed

    # рух ворога
    def update(self):
        self.rect.x += self.speed

        if self.rect.x > win_width + 10:
            self.kill()

class Enemy2(GameSprite):
    side = 'top'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    
    def update(self):
        if self.rect.y <= 20:
            self.side = 'bottom'
        if self.rect.y >= win_height/2 -100 :
            self.side = 'top'

        if self.side == 'top':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed




class Enemy1(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 660:
            self.side = 'right'
        if self.rect.x >= win_width - 80:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



win_width = 1024
win_height = 768
bg = display.set_mode((win_width, win_height ))
pic = transform.scale(image.load('fon.png'), (1024, 768))
display.set_caption("Mystery Castle")

#_____________________________________________
#Персонажі

cosmo = Player("wizardd.png", 75, 130, 10, 580,  0, 0 )

bullets = sprite.Group()
f1nish = GameSprite('portal.png', 140, 170, 390, win_height - 200)
monsters = sprite.Group()
monsters.add(Enemy1('enemy.png', 80, 80, 1000, win_height/2 -20, 10)) # ОСЬ ЦЕЙ НЕ ВІДОБРАЖАЄТЬСЯ
monsters.add(Enemy2('enemy.png', 70, 70, 200, 20, 7))  #готовий!!!!!!


walls = sprite.Group()
walls.add(GameSprite('11.jpg',50, 390, win_width/2 - win_width/3, win_height/2))
walls.add(GameSprite('11.jpg', 47, 190 + 50, win_width/2, 0))
walls.add(GameSprite('11.jpg',440, 50, win_width/2 - win_width/3, win_height/2))#2
walls.add(GameSprite('11.jpg', 196, 47, win_width/2 - 196, 130))
walls.add(GameSprite('11.jpg', 50, 192,(win_width/2 - win_width/3)+440 ,win_height/2))
walls.add(GameSprite('11.jpg', 50, 200, win_width - 200, 568 ))
walls.add(GameSprite('11.jpg', 196, 47, win_width/2-196, 130))
walls.add(GameSprite('11.jpg', 290, 47, win_width - 290, 130))
walls.add(GameSprite('11.jpg', 190, 47, 0, 130))

#_____________________________________________

finish = False

run = True
while run:
    
    for i in event.get(): 
        if i.type == QUIT:
            run = False
            
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                cosmo.fire()
            elif i.key == K_LEFT:
                cosmo.x_speed = -9
                
            elif i.key == K_RIGHT:
                cosmo.x_speed = 9
            elif i.key == K_DOWN:
                cosmo.y_speed = 9
            elif i.key == K_UP:
                cosmo.y_speed = -9
        elif i.type == KEYUP:
            if i.key == K_LEFT:
                cosmo.x_speed = 0
            elif i.key == K_RIGHT:
                cosmo.x_speed = 0
            elif i.key == K_UP:
                cosmo.y_speed = 0
            elif i.key == K_DOWN:
                cosmo.y_speed = 0


    if not finish:
        bg.blit(pic, (0,0))
        walls.draw(bg)
        bullets.draw(bg)
        bullets.update()
        f1nish.reset()
        cosmo.reset()
        cosmo.touch()
        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(bg)

        sprite.groupcollide(bullets, walls, True, False)

        if sprite.spritecollide(cosmo, monsters, False):
            finish = True
            img = image.load('gmovr.jpg')

            bg.blit(transform.scale(img, (win_width, win_height)), (0,0))

        if sprite.collide_rect(cosmo, f1nish):
            finish = True
            img = image.load('pngaaa.com-1226329.png')
            bg.fill((186,186,186))            
            bg.blit(transform.scale(img, (win_width, win_height)), (0,0))

        time.delay(40)
        display.update()