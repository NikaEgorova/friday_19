from pygame import*

class GameSprite(sprite.Sprite):
   
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        
        sprite.Sprite.__init__(self)
 
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprite.Sprite):
    def __init__(self, pictures, w, h, x, y, x_speed, y_speed, position, move):
        self.pictures = pictures
        self.image = transform.scale(image.load(pictures[move]), [w, h])
        self.move = move
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.position = position
    def update(self): 
        # Спершу рух по горизонталі
        if self.rect.x <= win_width-50 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
            # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barrier, False)
        if self.x_speed > 0: # йдемо праворуч, правий край персонажа - впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # якщо торкнулися відразу кількох, то правий край - мінімальний із можливих
        elif self.x_speed < 0: # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # якщо торкнулися кількох стін, то лівий край - максимальний
        if self.rect.y <= win_height-50 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barrier, False)
        if self.y_speed > 0: # йдемо вниз
            for p in platforms_touched:
                # Перевіряємо, яка з платформ знизу найвища, вирівнюємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # йдемо вгору
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) # вирівнюємо верхній край по нижніх краях стінок, на які наїхали
        self.x_speed = 0
        self.y_speed = 0
        
 # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        bullet = Bullet('пуля,обріз.png', self.rect.centerx, self.rect.top, 30, 10, 15)
        bullets.add(bullet)
    def draw(self):
        if self.position == 0:
            window.blit(self.image,(self.rect.x,self.rect.y))
        elif self.position == 1:
            window.blit(transform.flip(self.image,True,False),(self.rect.x,self.rect.y))
    def moves(self):
        self.image = transform.scale(image.load(self.pictures[self.move]), [self.w, self.h])

#клас спрайту-ворога
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.x <= 420: 
            self.side = "right"
        if self.rect.x >= win_width - 60:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.y <= 40: 
            self.side = "right"
        if self.rect.y >= win_height - 390:
            self.side = "left"
        if self.side == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy3(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.y <= 390: 
            self.side = "right"
        if self.rect.x >= win_width- 390:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed     

class Enemy4(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

   #рух ворога
    def update(self):
        if self.rect.x <= 40: 
            self.side = "right"
        if self.rect.x >= win_width - 390:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed                   
           

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

#Створюємо віконце
win_width = 1400
win_height = 800
display.set_caption("labirint")
back = transform.scale(image.load('кактус.png'), (1400, 800))
window = display.set_mode((win_width, win_height))


barrier = sprite.Group()

bullets =sprite.Group()

monsters = sprite.Group()


#w1 = GameSprite('стовп,малий.png', 100, 0, 50, 400)

Walk_Right = [
    'чорний право1.png',
    'право 2.png',
    'право 3.png' ,
    'право 4.png',
    'право 5.png'
]

animation = 0


#barrier.add(w1)
camerman = Player(Walk_Right, 78, 103, 100, 500, 0, 0, 0, 0)
#створюємо спрайти
monster1 = Enemy('бутиль.png', 650, 0, 50, 100, 0)#верхній
final_sprite = GameSprite('двері 1.png',1285 , 610, 100, 150)
monsters.add(monster1)
#змінна, що відповідає за те, як закінчилася гра
finish = False
#ігровий цикл
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    keys = key.get_pressed()
    if keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]:
        camerman.move += 1       
    if camerman.move >= 5:
        camerman.move = 0
    if keys[K_a] and keys[K_w]:
        camerman.x_speed = -10
        camerman.y_speed = -10
        camerman.position = 1
    elif keys[K_a] and keys[K_s]:
        camerman.x_speed = -10
        camerman.y_speed = 10
        camerman.position = 1
    elif keys[K_d] and keys[K_w]:
        camerman.x_speed = 10
        camerman.y_speed = -10
        camerman.position = 0
    elif keys[K_s] and keys[K_d]:
        camerman.x_speed = 10
        camerman.y_speed = 10
        camerman.position = 0 
    elif keys[K_a]:
        camerman.x_speed = -10
        camerman.position = 1
    elif keys[K_d]:
        camerman.x_speed = 10
        camerman.position = 0
    elif keys[K_w]:
        camerman.y_speed = -10
    elif keys[K_s]:
        camerman.y_speed = 10
    if (keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]) == False:
        camerman.move = 0
    if not finish:
        window.blit(back ,(0, 0))

        camerman.draw()
        camerman.moves()
        camerman.update()
        bullets.draw(window)
        barrier.draw(window)
        final_sprite.reset()

        sprite.groupcollide(monsters, bullets, True, True)

        bullets.update()

        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barrier, True, False)

        #Перевірка зіткнення героя з ворогом та стінами
        if sprite.spritecollide(camerman, monsters, False):
            finish = True

            # обчислюємо ставлення
            img = image.load('програв (2).jpg')
            d = img.get_width() // img.get_height()
            window.fill((0, 0, 0))
        
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
            

        if sprite.collide_rect(camerman, final_sprite):
            finish = True
            img = image.load('images.jpg')
            window.fill((0, 0, 0))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
        #цикл спрацьовує кожну 0.05 секунд
        time.delay(50)
        display.update()

