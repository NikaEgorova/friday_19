from pygame import *

#клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
    
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    #метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#клас головного гравця
class Player(GameSprite):
    #метод, у якому реалізовано управління спрайтом за кнопками стрілочкам клавіатури
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    ''' переміщає персонажа, застосовуючи поточну горизонтальну та вертикальну швидкість'''
    def update(self):  
        # Спершу рух по горизонталі
        if mario.rect.x <= win_width-50 and mario.x_speed > 0 or mario.rect.x >= 0 and mario.x_speed < 0:
            self.rect.x += self.x_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # йдемо праворуч, правий край персонажа - впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # якщо торкнулися відразу кількох, то правий край - мінімальний із можливих
        elif self.x_speed < 0: # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # якщо торкнулися кількох стін, то лівий край - максимальний
        if mario.rect.y <= win_height-50 and mario.y_speed > 0 or mario.rect.y >= 0 and mario.y_speed < 0:
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # йдемо вниз
            for p in platforms_touched:
                # Перевіряємо, яка з платформ знизу найвища, вирівнюємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # йдемо вгору
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) # вирівнюємо верхній край по нижніх краях стінок, на які наїхали
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        bullet = Bullet('bullets.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

#клас спрайту-ворога
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_x1, start_x2):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2

   #рух ворога
    def update(self):
        if self.rect.x <= self.start_x1: 
            self.side = "right"
        if self.rect.x >= win_width - self.start_x2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
class Enemy1(GameSprite):
    side = "up"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_y1, start_y2):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_y1=start_y1
        self.start_y2=start_y2

   #рух ворога
    def update(self):
        if self.rect.y <= self.start_y1: 
            self.side = "down"
        if self.rect.y >= self.start_y2:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

# клас спрайту-кулі
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.x > win_width+10:
            self.kill()

win_width = 720
win_height = 720
display.set_caption("Лабіринт")
window = display.set_mode((win_width, win_height))
back=transform.scale(image.load("fon.jpg"), (720, 720))

#Створюємо групу для стін
barriers = sprite.Group()

#життя
heall = 3

#ключі
kcey1 = 0

#лвл
level = 1

#створюємо групу для куль
bullets = sprite.Group()

#Створюємо групу для монстрів
mushrooms = sprite.Group()

#ключ
kceys = sprite.Group()

#життя
heall1 = GameSprite('heall.png',0,0,50,50)
heall2 = GameSprite('heall.png',50,0,50,50)
heall3 = GameSprite('heall.png',100,0,50,50)

#ключ
kcey = GameSprite('key.png',405,110,50,50)

#огорожа
ww1 = GameSprite('wall.jpg',0, 60, 160, 10)
ww2 = GameSprite('wall.jpg',160, 0, 10, 70)

#Створюємо стіни картинки
w1 = GameSprite('wall.jpg',0, 480, 170, 10)
w2 = GameSprite('wall.jpg', 60, 550, 10, 180)
w3 = GameSprite('wall.jpg',130, 550, 100, 10)
w4 = GameSprite('wall.jpg',230, 370, 10, 290)
w5 = GameSprite('wall.jpg',130, 550, 10, 110)
w6 = GameSprite('wall.jpg',230, 650, 280, 10)
w7 = GameSprite('wall.jpg',560, 580, 80, 10)
w8 = GameSprite('wall.jpg',560, 100, 10, 560)
w9 = GameSprite('wall.jpg',640, 650, 90, 10)
w10 = GameSprite('wall.jpg',310, 580, 250, 10)
w11 = GameSprite('wall.jpg',640, 500, 80, 10)
w12 = GameSprite('wall.jpg',560, 420, 80, 10)
w13 = GameSprite('wall.jpg',640, 340, 80, 10)
w14 = GameSprite('wall.jpg',560, 260, 80, 10)
w15 = GameSprite('wall.jpg',640, 180, 80, 10)
w16 = GameSprite('wall.jpg',560, 100, 80, 10)
w17 = GameSprite('wall.jpg',220, 100, 180, 10)
w18 = GameSprite('wall.jpg',470, 100, 90, 10)
w19 = GameSprite('wall.jpg',240, 510, 250, 10)
w20 = GameSprite('wall.jpg',310, 440, 180, 10)
w21 = GameSprite('wall.jpg',70, 370, 420, 10)
w22 = GameSprite('wall.jpg',470, 110, 90, 60)
w23 = GameSprite('wall.jpg',390, 110, 10, 130)
w24 = GameSprite('wall.jpg',400, 160, 70, 10)
w25 = GameSprite('wall.jpg',70, 160, 10, 210)
w26 = GameSprite('wall.jpg',70, 160, 230, 10)
w27 = GameSprite('wall.jpg',150, 230, 250, 90)
w28 = GameSprite('wall.jpg',480, 230, 10, 150)


#обманка(стіна)
inviz1 = GameSprite('inviz.png',500, 650, 10, 70)
inviz2 = GameSprite('inviz.png',560, 650, 80, 10)
inviz3 = GameSprite('inviz.png',480, 440, 80, 10)

#обманка(стіни)
barriers.add(inviz1)
barriers.add(inviz2)
barriers.add(inviz3)


#додаємо стіни,ключ до групи
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
barriers.add(w23)
barriers.add(w24)
barriers.add(w25)
barriers.add(w26)
barriers.add(w27)
barriers.add(w28)

barriers.add(ww1)
barriers.add(ww2)

kceys.add(kcey)
#створюємо спрайти
mario = Player('mario.png', 5, win_height - 50, 50, 50, 0, 0)
mushroom1 = Enemy('mushroom.png', win_width - 650, 670, 50, 50, 5, 70,110)
mushroom2 = Enemy('mushroom.png', win_width - 100, 0, 100, 100, 5, 170, 100)
mushroom3 = Enemy1('mushroom.png', win_width - 220, 170, 50, 50, 5, 170, 530)
tube = GameSprite('tube.png', win_width - 70, win_height - 60, 100, 80)

#додаємо монстра до групи
mushrooms.add(mushroom1)
mushrooms.add(mushroom2)
mushrooms.add(mushroom3)

#змінна, що відповідає за те, як закінчилася гра
finish = False
#ігровий цикл
run = True
while run:
    #цикл спрацьовує кожну 0.05 секунд
        time.delay(50)
            #перебираємо всі події, які могли статися
        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_LEFT:
                    mario.x_speed = -5
                elif e.key == K_RIGHT:
                    mario.x_speed = 5
                elif e.key == K_UP:
                    mario.y_speed = -5
                elif e.key == K_DOWN:
                    mario.y_speed = 5
                elif e.key == K_SPACE:
                    mario.fire()


            elif e.type == KEYUP:
                if e.key == K_LEFT:
                    mario.x_speed = 0
                elif e.key == K_RIGHT:
                    mario.x_speed = 0 
                elif e.key == K_UP:
                    mario.y_speed = 0
                elif e.key == K_DOWN:
                    mario.y_speed = 0
        
    #перевірка, що гра ще не завершена
        if not finish:
            #оновлюємо фон кожну ітерацію
            window.blit(back,(0,0))
            
            #запускаємо рухи спрайтів
            mario.update()
            bullets.update()

            #оновлюємо їх у новому місці при кожній ітерації циклу
            mario.reset()
            #рисуємо стіни 2
            bullets.draw(window)
            barriers.draw(window)
            kceys.draw(window)
            tube.reset()
            if heall == 3:
                heall1.reset()
                heall2.reset()
                heall3.reset()
            elif heall == 2:
                heall1.reset()
                heall2.reset()
            else:
                heall1.reset()

            sprite.groupcollide(mushrooms, bullets, True, True)
            mushrooms.update()
            mushrooms.draw(window)
            sprite.groupcollide(bullets, barriers, True, False)

            #підбір ключа
            if sprite.spritecollide(mario, kceys, True):
                kcey1 +=1

            #Перевірка зіткнення героя з ворогом та стінами
            if sprite.spritecollide(mario, mushrooms, False):
                heall-=1

                if heall > 0 :
                    mario = Player('mario.png', 5, win_height - 50, 50, 50, 0, 0)
                    if kcey1 == 1:
                        kcey1 -=1
                        kcey = GameSprite('key.png',405,110,50,50)
                        kceys.add(kcey)
                        

                else:
                    finish = True
                    img = image.load('game-over.jpg')
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))   

            if sprite.collide_rect(mario, tube) and kcey1 == 1:
                finish = True
                img = image.load('win.jpg')
                window.blit(transform.scale(img, (win_width, win_height)),(0, 0))
            display.update()

        
            