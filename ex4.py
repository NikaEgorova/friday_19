# Розроби свою гру в цьому файлі!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pizza), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pizza_x
        self.rect.y = pizza_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

display.set_caption('Лабіринт')
window = display.set_mode((700, 500))
back = transform.scale(image.load('Background5.jpg'),(700, 500))
barriers = sprite.Group()

class Player(GameSprite):
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y, pizza_x_speed, pizza_y_speed):
        GameSprite.__init__(self, pizza, pizza_x, pizza_y, size_x, size_y)
        self.x_speed = pizza_x_speed
        self.y_speed = pizza_y_speed

    def update(self):
        if mypizza.rect.x <= 630 and mypizza.x_speed > 0 or mypizza.rect.x >= 0 and mypizza.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if mypizza.rect.y <= 430 and mypizza.y_speed > 0 or mypizza.rect.y >= 0 and mypizza.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('sliced-tomato2.png', self.rect.right - 25, self.rect.centery - 16, 15, 13, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y, pizza_speed):
        self.speed = pizza_speed
        GameSprite.__init__(self, pizza, pizza_x, pizza_y, size_x, size_y)

    def update(self):
        if self.rect.x <= 200:
            self.side = 'right'
        if self.rect.x >= 520:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = 'left'
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y, pizza_speed):
        self.speed = pizza_speed
        GameSprite.__init__(self, pizza, pizza_x, pizza_y, size_x, size_y)

    def update(self):
        if self.rect.x <= 10:
            self.side = 'right'
        if self.rect.x >= 350:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy3(GameSprite):
    side = 'left'
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y, pizza_speed):
        GameSprite.__init__(self, pizza, pizza_x, pizza_y, size_x, size_y)
        self.speed = pizza_speed

    def update(self):
        if self.rect.y <= 75:
            self.side = 'down'
        if self.rect.y >= 280:
            self.side = 'up'
        if self.side == 'up':
            self.rect.y -= self.speed
        elif self.side == 'down':
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, pizza, pizza_x, pizza_y, size_x, size_y, pizza_speed):
        self.speed = pizza_speed
        GameSprite.__init__(self, pizza, pizza_x, pizza_y, size_x, size_y)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 710:
            self.kill()


mypizza = Player('pizza2.png', 5, 5, 65, 65, 0, 0)
knife = Enemy3('knife.png', 610, 20, 75, 75, 6)
knife2 = Enemy2('knife.png', 20, 427, 70, 70, 5)
knife3 = Enemy('knife.png', 200, 195, 65, 65, 5)
prize = GameSprite('tomato2.png', 620, 420, 60, 70)

bullets = sprite.Group()

knives = sprite.Group()
knives.add(knife)
knives.add(knife2)
knives.add(knife3)

barriers.add(GameSprite('cutting-board70.png', 350, 90, 30, 80))
barriers.add(GameSprite('cutting-board80.png', 0, 70, 380, 30))
barriers.add(GameSprite('cutting-board80.png', 400, 360, 300, 30))
barriers.add(GameSprite('cutting-board80.png', 150, 165, 230, 30))
barriers.add(GameSprite('cutting-board80.png', 0, 260, 600, 30))
barriers.add(GameSprite('cutting-board80.png', 140, 395, 120, 30))
barriers.add(GameSprite('cutting-board70.png', 400, 365, 30, 60))
barriers.add(GameSprite('cutting-board70.png', 510, 0, 30, 195))
barriers.add(GameSprite('cutting-board80.png', 540, 165, 60, 30))

Finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                mypizza.x_speed = -10
            elif e.key == K_RIGHT:
                mypizza.x_speed = 10
            elif e.key == K_UP:
                mypizza.y_speed = -10
            elif e.key == K_DOWN:
                mypizza.y_speed = 10
            elif e.key == K_SPACE:
                mypizza.fire()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                mypizza.x_speed = 0
            elif e.key == K_RIGHT:
                mypizza.x_speed = 0
            elif e.key == K_UP:
                mypizza.y_speed = 0
            elif e.key == K_DOWN:
                mypizza.y_speed = 0
    
    if not Finish:
        window.blit(back, (0, 0))
        barriers.draw(window)
        bullets.draw(window)
        bullets.update()
        mypizza.reset()
        mypizza.update()
        prize.reset()

        sprite.groupcollide(knives, bullets, True, True)
        knives.update()
        knives.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)

        if sprite.spritecollide(mypizza, knives, False):
            Finish = True
            lose = image.load('you-lose2.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(lose, (700, 500)), (0, 0))

        if sprite.collide_rect(mypizza, prize):
            Finish = True
            win = image.load('you-win.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(win, (700, 500)), (0, 0))
        
        time.delay(50)
        display.update()