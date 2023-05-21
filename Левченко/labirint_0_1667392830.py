from pygame import *

width = 700
height = 500
scene = display.set_mode((width, height))
display.set_caption('Labyrinth')
background_image = image.load('background.jpg')
black = (0, 0, 0)
brown = (139, 69, 19)
font.init()
font = font.SysFont('Vogue', 30)
tap = font.render('Tap space to restart', True, black)
rule = font.render('5x        =', True, brown)


class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self):
        scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        Sprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if character[ch].rect.x <= width-80 and character[ch].x_speed > 0 or character[ch].rect.x >= 0 and character[ch].x_speed < 0:
            self.rect.x += self.x_speed
        touched_area = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for i in touched_area:
                self.rect.right = min(self.rect.right, i.rect.left)
        elif self.x_speed < 0:
            for i in touched_area:
                self.rect.left = max(self.rect.left, i.rect.right)
        if character[ch].rect.y <= height - 80 and character[ch].y_speed > 0 or character[ch].rect.y >= 0 and character[ch].y_speed < 0:
            self.rect.y += self.y_speed
        touched_area = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for i in touched_area:
                if i.rect.top < self.rect.bottom:
                    self.rect.bottom = i.rect.top
        elif self.y_speed < 0:
            for i in touched_area:
                self.rect.top = max(self.rect.top, i.rect.bottom)

class Enemy_x(Sprite):
    side1 = 'right'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        Sprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 250:
            self.side1 = 'right'
        if self.rect.x >= width - 165:
            self.side1 = 'left'

        if self.side1 == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Character(Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        Sprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
    def collidepoint(player_x, player_y):
        return self.player_image.collidepoint(x, y)

class Berry(Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        Sprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

wall1 = Sprite('linee.PNG', 90, 250, 30, 150)
wall2 = Sprite('line.PNG', 93, 240, 150, 30)
wall3 = Sprite('linee.PNG', 216, 350, 30, 150)
wall4 = Sprite('line.PNG', 219, 345, 150, 30)
wall5 = Sprite('linee.PNG', 219, 117, 30, 150)
wall6 = Sprite('linee.PNG', 342, 220, 30, 150)
wall7 = Sprite('line.PNG', 97, 100, 150, 30)
wall8 = Sprite('linee.PNG', 342, -30, 30, 150)
wall9 = Sprite('linee.PNG', 450, 220, 30, 150)
wall10 = Sprite('line.PNG', 454, 345, 150, 30)
wall11 = Sprite('line.PNG', 345, 100, 150, 30)
wall12 = Sprite('linee.PNG', 450, 350, 30, 150)
wall13 = Sprite('linee.PNG', 578, -25, 30, 150)
wall14 = Sprite('linee.PNG', 578, 220, 30, 150)
wall15 = Sprite('linee.PNG', 578, 350, 30, 150)

berry1 = Berry('berry.PNG', 150, 180, 25, 25)
berry2 = Berry('berry.PNG', 300, 430, 25, 25)
berry3 = Berry('berry.PNG', 450, 40, 25, 25)
berry4 = Berry('berry.PNG', 512, 270, 25, 25)
berry5 = Berry('berry.PNG', 625, 150, 25, 25)

ch = 0
character = list()
enemy = list()
food = list()
berries = sprite.Group()

def start():
    global character
    global enemy
    global food
    global berries
    character = list()
    enemy = list()
    food = list()
    character.append(Player('pig.PNG', 5, height - 80, 70, 70, 0, 0))
    character.append(Player('cow.PNG', 5, height - 80, 70, 70, 0, 0))
    character.append(Player('chicken.PNG', 5, height - 60, 60, 60, 0, 0))
    character.append(Player('goat.PNG', 5, height - 80, 70, 70, 0, 0))
    enemy.append(Enemy_x('enemy2.PNG', width - 200, 130, 70, 70, 5))
    enemy.append(Enemy_x('enemy4.PNG', width - 200, 130, 70, 70, 5))
    enemy.append(Enemy_x('enemy.PNG', width - 200, 130, 70, 70, 5))
    enemy.append(Enemy_x('enemy3.PNG', width - 200, 130, 70, 70, 5))

    food.append(Sprite('food.PNG', width - 85, height - 100, 80, 80))
    food.append(Sprite('food1.PNG', width - 85, height - 100, 80, 80))
    food.append(Sprite('food2.PNG', width - 85, height - 100, 80, 80))
    food.append(Sprite('food3.PNG', width - 85, height - 100, 80, 80))

    berries.add(berry1)
    berries.add(berry2)
    berries.add(berry3)
    berries.add(berry4)
    berries.add(berry5)

barriers = sprite.Group()
barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall7)
barriers.add(wall8)
barriers.add(wall9)
barriers.add(wall10)
barriers.add(wall11)
barriers.add(wall12)
barriers.add(wall13)
barriers.add(wall14)
barriers.add(wall15)

def menu():
    menu = image.load('menu.jpg')
    berry_for_menu = Character('berry.PNG', 48, 457, 25, 25)
    food_for_menu = Character('food.PNG', 100, 448, 50, 50)
    play = True
    char1 = Character('pig.PNG', 240, 250, 100, 100)
    char2 = Character('cow.PNG', 100, 250, 100, 100)
    char3 = Character('chicken.PNG', 380, 250, 80, 100)
    char4 = Character('goat.PNG', 510, 250, 100, 100)
    scene.blit(menu, (-25, 0))
    time.delay(50)
    char1.reset()
    char2.reset()
    char3.reset()
    char4.reset()
    scene.blit(rule, (15, 463))
    berry_for_menu.reset()
    food_for_menu.reset()
    display.update()
    while play:
        for e in event.get():
            if e.type == QUIT:
                play = False
            elif e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if 240 < x < 350 and 240 < y < 350:
                    return 0
                elif 100 < x < 200 and 250 < y < 350:
                    return 1
                elif 380 < x < 460 and 250 < y < 350:
                    return 2
                elif 510 < x < 610 and 250 < y < 350:
                    return 3
    

def game():
    berries_amount = 0
    play = True
    finish = False
    while play:
        for e in event.get():
            if e.type == QUIT:
                return False 
            elif e.type == KEYDOWN:
                if e.key == K_w:
                    character[ch].y_speed = -5
                elif e.key == K_s:
                    character[ch].y_speed = 5
                elif e.key == K_a:
                    character[ch].x_speed = -5
                elif e.key == K_d:
                    character[ch].x_speed = 5
            elif e.type == KEYUP:
                if e.key == K_w:
                    character[ch].y_speed = 0
                elif e.key == K_s:
                    character[ch].y_speed = 0
                elif e.key == K_a:
                    character[ch].x_speed = 0
                elif e.key == K_d:
                    character[ch].x_speed = 0
        if not finish:
            scene.blit(background_image, (0, 0))
            barriers.draw(scene)
            berries.draw(scene)
            enemy[ch].update()
            enemy[ch].reset()
            food[ch].reset()
            character[ch].reset()
            character[ch].update()

        if sprite.collide_rect(character[ch], enemy[ch]):
            finish = True
            return False 

        if sprite.spritecollide(character[ch], berries, True):
            berries_amount += 1

        if berries_amount == 5:
            if sprite.collide_rect(character[ch], food[ch]):
                finish = True
                return True
        time.delay(50)
        display.update()

def finish(game_result):
    if game_result == True:
        if ch == 0:
            pic = image.load('winner.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 1:
            pic = image.load('winner3.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 2:
            pic = image.load('winner2.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 3:
            pic = image.load('winner1.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
    elif game_result == False:
        if ch == 0:
            pic = image.load('gameover.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 1:
            pic = image.load('gameover1.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 2:
            pic = image.load('gameover2.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
        elif ch == 3:
            pic = image.load('gameover3.JPG')
            scene.blit(transform.scale(pic, (width, height)), (0, 0))
            scene.blit(tap, (10, 475))
    time.delay(50)
    display.update()

    while True:
        for e in event.get():
            if e.type == QUIT:
                return False 
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    return True
    
while True:
    start()
    ch = menu()
    if not finish(game()):
        break