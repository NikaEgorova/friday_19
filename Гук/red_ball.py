from pygame import *
from pygame import mixer
window = display.set_mode((800,500))
display.set_caption('pretend to red ball 4')

phon = transform.scale(image.load('fon.png'), (800, 500))
phon_L1 = transform.scale(image.load('underground.jpg'), (800, 500))
phon_L2 = transform.scale(image.load('ground.png'), (900, 600))
phon_L3 = transform.scale(image.load('fon.png'), (800, 500))
phon_L4 = transform.scale(image.load('sky.jpg'), (800, 500))
phon_L5 = transform.scale(image.load('space_phon.jpg'), (800, 500))
final = transform.scale(image.load('gameOver.png'), (800, 500))
phon_Win = transform.scale(image.load('win_you.png'), (800, 500))

click = 0
clock = time.Clock()
mixer.init()
run = True

scroll = 1
scroll_X = 1
scroll_Y = 1
scroll_Y_2 = 1
scroll_Y_5 = 1
scroll_Y_6 = 1



class GameSprite(sprite.Sprite):
    def __init__(self, picture, wight, hieght, x, y, angle):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(picture), (wight, hieght))
        self.rect = self.image.get_rect()
        self.angle = angle
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def moving(self):
        variable_x = True
        if variable_x == True:
            image_2 = transform.rotate(self.image, self.angle)
            window.blit(image_2, ((self.rect.x), (self.rect.y)))


class Button():
    def __init__(self, picture, widht, height, x, y, scaleW, scaleH):
        self.wight = widht
        self.height = height
        self.image = image.load(picture)
        self.image = transform.scale(self.image, (widht, height))
        self.rect = self.image.get_rect()
        self.scaleW = scaleW
        self.scaleW = scaleH
        self.image2 = transform.scale(image.load(picture), (scaleW, scaleH))
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        agree = True
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            agree = False
            window.blit(self.image2, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))
        return agree

class Player(GameSprite):
    def __init__(self, picture, wight, hight, x, y, speed_x, speed_y, angle):
        GameSprite.__init__(self, picture, wight, hight, x, y, angle)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        global M_L
        global R
        global click 
        global run
        keys = key.get_pressed()
        if keys[K_SPACE]:
            self.speed_y = 0
        elif keys[K_RIGHT]:
            self.angle -=5
        elif keys[K_LEFT]:
            self.angle +=5
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.speed_x = 10
                    self.angle -=5
                elif e.key == K_LEFT:
                    self.speed_x = -10
                    self.angle += 5
                elif e.key == K_SPACE:
                    self.angle = 0
                    self.speed_y = -90
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.speed_x = 0
                elif e.key == K_LEFT:
                    self.speed_x = 0
                elif e.key == K_SPACE:
                    self.angle = 0
                    self.speed_y = 90
            elif e.type == MOUSEBUTTONDOWN and M_L == False and click == 0:
                music.not_sing()
                click = 1
            elif e.type == MOUSEBUTTONDOWN and M_L == False and click == 1:
                music.sing()
                click = 0 
            elif e.type == QUIT:
                run = False 


        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 740:
            self.rect.x = 740
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 420:
            self.rect.y = 420
        

        touched = sprite.spritecollide(self, bariers, False)
        if self.speed_y > 0:
            for p in touched:
                self.rect.bottom = p.rect.top
        else:
            if self.speed_x > 0:
                for p in touched:
                    self.rect.right = p.rect.left
            elif self.speed_x < 0:
                for p in touched:
                    self.rect.left = p.rect.right

        if self.speed_y < 0:
            for p in touched:
                self.rect.top = p.rect.bottom


class Musik():
    def __init__(self, song):
        self.song = song
    def sing(self):
        mixer.music.load(self.song)
        mixer.music.play()
    def not_sing(self):
        mixer.music.load(self.song)
        mixer.music.stop()

class Beg():
    def __init__(self, picture, wight, hieght, x, y, scroll):
        self.image = transform.scale(image.load(picture), (wight, hieght))
        self.wight = wight
        self.hieght = hieght
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.scroll = scroll

# class Enemy(GameSprite):
#     def __init__(self, picture, wight, hight, x, y, speed_x, speed_y, angle, stop_1,stop_2):
#        GameSprite.__init__(self, picture, wight, hight, x, y, angle)
#        self.speed_x = speed_x
#        self.speed_y = speed_y
#        self.stop_1 = stop_1
#        self.stop_2 = stop_2
#        self.side = 'right'
#     def update(self):
#         panel = False
#         if self.rect.y == hero_play.rect.y:
#             self.speed_x = 1
            
#         if self.rect.x > self.stop_1:
#             self.side = 'left'
#         elif self.rect.x < self.stop_2:
#             self.side = 'right'

#         if self.side == 'right':
#             self.rect.x+=self.speed_x
#         else:
#             self.rect.x-= self.speed_x


button = Button('playRed.png', 100, 100, 350, 250, 110, 110)
hero = GameSprite('red_ball.png', 80, 80, 0, 370, 45)
level1 = Button('level1.png', 50, 50, 100, 100, 60, 60)
level2 = Button('level2.png', 50, 50, 220, 100, 60, 60)
level3 = Button('level3.png', 50, 50, 340, 100, 60, 60)
level4 = Button('level4.png', 50, 50, 460, 100, 60, 60)
level5 = Button('level5.png', 50, 50, 580, 100, 60, 60)
key_img = GameSprite('key.move.png', 150, 100, 100, 100, 45)
key_Jump = GameSprite('key.jump.png', 150, 100, 350, 100, 45)
Go = Button('start.png', 100, 100, 600, 300, 110, 110)
grass = GameSprite('wall.png', 200, 50, 0,350, 0)
hero_play = Player('red_ball.png', 70, 70, 0, 420, 0, 0, 45)
hero_play2 = Player('red_ball.png', 70, 70, 0, 420, 0, 0, 45)
hero_play_3 = Player('red_ball.png', 70, 70, 500, 420, 0, 0, 45)
hero_play_4 = Player('red_ball.png', 70, 70, 0, 380, 0, 0, 45)
hero_play_5 = Player('red_ball.png', 70, 70, 0, 400, 0, 0, 45)
music_L =  Button('loud.png', 20, 20, 700, 50, 20, 20)
music = Musik('Menu.mp3')
cub1 = GameSprite('undrground_wall.png', 750, 30, 100, 400, 0)
cub2 = GameSprite('undrground_wall.png', 700, 30, 0, 310, 0)
cub3 = GameSprite('undrground_wall.png', 100, 30, 150, 220, 0)
cub4 = GameSprite('undrground_wall.png', 100, 30, 300, 160, 0)
cub5 = GameSprite('undrground_wall.png', 500, 30, 470, 70, 0)
Next = GameSprite('undrground_wall.png', 70, 70, 800, 30, 0)
exit2 = GameSprite('sky.jpg', 1000, 70, 0, 480, 0)
holl = GameSprite('down.png', 200, 100, 500, -40, 0)
grass_block = GameSprite('wall.png', 200, 100, 300, 310, 0)
spiker = GameSprite('spikes.png', 70, 50, 0, 25, 90)
spiker2 = GameSprite('spikes.png', 70, 50, 0, 75, 90)
spiker3 = GameSprite('spikes.png', 70, 50, 0, 125, 90)
spiker4 = GameSprite('spikes.png', 70, 50, 0, 175, 90)
grass_block2 = GameSprite('wall.png', 200, 100, 600, 400, 0)
returnn = Button('back_home.png', 100, 100, 350, 300, 110, 110)
stone = GameSprite('stone.png', 130, 150, 100, 400, 0)
spiker_L2 = GameSprite('spikes.png', 70, 50, 0, 350, 0)
spiker_L2_2 = GameSprite('spikes.png', 70, 50, 100, 350, 0)
spiker_L2_3 = GameSprite('spikes.png', 70, 50, 200, 350, 0)
spiker_L2_4 = GameSprite('spikes.png', 70, 50, 300, 350, 0)
spiker_L2_5 = GameSprite('spikes.png', 70, 50, 400, 350, 0)
basis_spikes = GameSprite('undrground_wall.png', 600, 30, 0, 320, 0)
lift_X = GameSprite('undrground_wall.png', 150, 30, 0, 230, 0)
fly_block =  GameSprite('fly_block.png', 100, 100, 0, 450, 0)
fly_block2 =  GameSprite('fly_block.png', 100, 50, 200, 400, 0)
fly_block3 =  GameSprite('fly_block.png', 100, 50, 450, 400, 0)
fly_block5 =  GameSprite('fly_block.png', 100, 50, 650, 400, 0)
laserGood =  GameSprite('blue_laser.png', 200, 40, -70, 80, 0)
laserGood_basis =  GameSprite('blue_laser.png', 1200, 50, -300, 470, 0)
laserGood_lift = GameSprite('blue_laser.png', 250, 40, 0, 200, 0)
laserBad = GameSprite('red_laser.png', 50, 190, 300, 210, 0)
space_stone = GameSprite('stone.png', 120, 120, 680, 380, 0)
jump = GameSprite('jump.png', 150, 100, 300, 250, 0)
move = GameSprite('move.png', 150, 100, 100, 250, 0)

bariers = sprite.Group()
bariers.add(lift_X)

spikers_wall = sprite.Group()


change = 1

change_music = False
music.sing()
M_L = music_L.draw()

Text = transform.scale(image.load("text.png"), (500, 200))
sound = True
while run:

    if change == 1:
        window.blit(phon,(0,0))
        window.blit(Text,(180,80))
        button.draw()
        hero.angle-=1
        hero.rect.x+=5
        hero.moving()
        B = button.draw()
        music_L.draw()
        M_L = music_L.draw()
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and M_L == False and click == 0:
                music.not_sing()
                click = 1
            elif e.type == MOUSEBUTTONDOWN and M_L == False and click == 1:
                music.sing()
                click = 0
            elif e.type == MOUSEBUTTONDOWN and B == False:
                change = 2
            elif e.type == QUIT:
                run = False
    if change == 2:
        window.blit(phon,(0,0))
        instruction = Rect(50, 50, 700, 400)
        draw.rect(window, (0, 0, 0), instruction)
        jump.reset()
        move.reset()
        key_img.reset()
        key_Jump.reset()
        Go.draw()
        G = Go.draw()
        music_L.draw()
        M_L = music_L.draw()
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and M_L == False and click == 0:
                music.not_sing()
                click = 1
            elif e.type == MOUSEBUTTONDOWN and M_L == False and click == 1:
                music.sing()
                click = 0
            elif e.type == MOUSEBUTTONDOWN and G == False:
                change = 3
            elif e.type == QUIT:
                run = False
    if change == 3:
        window.blit(phon,(0,0))
        level1.draw()
        level2.draw()
        level3.draw()
        level4.draw()
        level5.draw()
        L1 = level1.draw()
        L2 = level2.draw()
        L3 = level3.draw()
        L4 = level4.draw()
        L5 = level5.draw()
        music_L.draw()
        M_L = music_L.draw()
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and M_L == False and click == 0:
                music.not_sing()
                click = 1
            elif e.type == MOUSEBUTTONDOWN and M_L == False and click == 1:
                music.sing()
                click = 0
            elif e.type == MOUSEBUTTONDOWN and L1 == False:
                change = 4
                change_music = True
                if change_music == True:
                    music.song = 'song_L1.mp3'
                    music.sing()
                    if click == 1:
                        music.not_sing() 
                        change_music = False
            elif e.type == MOUSEBUTTONDOWN and L2 == False:
                change = 5
            elif e.type == MOUSEBUTTONDOWN and L3 == False:
                change = 6
            elif e.type == MOUSEBUTTONDOWN and L4 == False:
                change = 7
            elif e.type == MOUSEBUTTONDOWN and L5 == False:
                change = 8
            elif e.type == QUIT:
                run = False
    if change == 4:
        window.blit(phon_L1,(0,0))
        # square.reset()
        # square.update()
        bariers.add(cub1)
        bariers.add(cub2)
        bariers.add(cub3)
        bariers.add(cub4)
        bariers.add(cub5)
        cub1.reset()
        cub2.reset()
        cub3.reset()
        cub4.reset()
        cub5.reset()
        Next.reset()
        hero_play.moving()
        hero_play.update()
        music_L.draw()
        M_L = music_L.draw()

        if sprite.collide_rect(hero_play,Next):
            change = 5

    if change == 5:
        window.blit(phon_L2,(-10,-10))
        music_L.draw()
        M_L = music_L.draw()
        holl.reset()
        bariers.remove(cub1)
        bariers.remove(cub2)
        bariers.remove(cub3)
        bariers.remove(cub4)
        bariers.remove(cub5)

        spiker_L2.reset()
        spiker_L2_2.reset()
        spiker_L2_3.reset()
        spiker_L2_4.reset()
        spiker_L2_5.reset()

        spikers_wall.add(spiker_L2)
        spikers_wall.add(spiker_L2_2)
        spikers_wall.add(spiker_L2_3)
        spikers_wall.add(spiker_L2_4)
        spikers_wall.add(spiker_L2_5)

        basis_spikes.reset()
        lift_X.reset()
        bariers.add(basis_spikes)
        stone.reset()
        hero_play2.moving()
        hero_play2.update()
        if sprite.collide_rect(hero_play2,stone):
            if hero_play2.speed_y > 0:
                hero_play2.rect.bottom = stone.rect.top
            if hero_play2.speed_x >0 :
                hero_play2.rect.right = stone.rect.left
                stone.rect.x+=2
        if stone.rect.x > 670:
            stone.rect.x = 670

        if scroll_X == 1:
            lift_X.rect.x+=3
            if lift_X.rect.x == 600:
                scroll_X = 2
        elif scroll_X == 2:
            lift_X.rect.y-=2
            if lift_X.rect.y == 50:
                scroll_X = 3
        elif scroll_X == 3:
            lift_X.rect.y+=2
            if lift_X.rect.y == 230:
                scroll_X = 4
        elif scroll_X == 4:
            lift_X.rect.x-=3
            if lift_X.rect.x == 0:
                scroll_X = 1


        if sprite.collide_rect(hero_play2,holl):
            change = 6
        
        if sprite.spritecollide(hero_play2,spikers_wall,False):
            hero_play2.rect.x = 0
            hero_play2.rect.y = 420
            hero_play2.speed_x = 0
            hero_play2.speed_y = 0
            change = 0

        


    if change == 6:
        window.blit(phon,(0,0))
        music_L.draw()
        M_L = music_L.draw()
        bariers.add(grass)
        bariers.add(grass_block)
        bariers.add(grass_block2)

        spikers_wall.add(spiker)
        spikers_wall.add(spiker2)
        spikers_wall.add(spiker3)
        spikers_wall.add(spiker4)
        spikers_wall.remove(spiker_L2)
        spikers_wall.remove(spiker_L2_2)
        spikers_wall.remove(spiker_L2_3)
        spikers_wall.remove(spiker_L2_4)

        bariers.remove(cub1)
        bariers.remove(cub2)
        bariers.remove(cub3)
        bariers.remove(cub4)
        bariers.remove(cub5)
        bariers.remove(basis_spikes)
        bariers.remove(lift_X)
        grass.reset()
        grass_block.reset()
        grass_block2.reset()
        spiker.moving()
        spiker2.moving()
        spiker3.moving()
        spiker4.moving()
        hero_play_3.moving()
        hero_play_3.update()
        if scroll == 1:
            grass.rect.y-=2
            if grass.rect.y == 50:
                scroll = 2
        elif scroll == 2:
            grass.rect.y+=2
            if grass.rect.y == 250:
                scroll = 1

        if hero_play_3.rect.y == 0:
            change = 7

        if sprite.spritecollide(hero_play_3,spikers_wall,False):
            hero_play_3.rect.x = 500
            hero_play_3.rect.y = 420
            hero_play_3.speed_x = 0
            hero_play_3.speed_y = 0
            change = 0
    if change == 7:
        window.blit(phon_L4,(0,0))
        music_L.draw()
        M_L = music_L.draw()
        bariers.remove(grass)
        bariers.remove(grass_block)
        bariers.remove(grass_block2)
        bariers.remove(cub1)
        bariers.remove(cub2)
        bariers.remove(cub3)
        bariers.remove(cub4)
        bariers.remove(cub5)
        bariers.remove(basis_spikes)
        bariers.remove(lift_X)
        bariers.add(fly_block)
        bariers.add(fly_block2)
        bariers.add(fly_block3)
        bariers.add(fly_block5)
        fly_block.reset()
        fly_block2.reset()
        fly_block3.reset()
        fly_block5.reset()
        exit2.reset()
        hero_play_4.moving()
        hero_play_4.update()
        if scroll_Y == 1:
            fly_block2.rect.y-=3
            if fly_block2.rect.y < 70:
                scroll_Y = 2
        elif scroll_Y == 2:
            fly_block2.rect.y+=3
            if fly_block2.rect.y > 400:
                scroll_Y = 1

        if scroll_Y_2 == 1:
            fly_block3.rect.y-=7
            if fly_block3.rect.y < 200:
                scroll_Y_2  = 2
        elif scroll_Y_2 == 2:
            fly_block3.rect.y+=7
            if fly_block3.rect.y > 550:
                scroll_Y_2 = 1

        if scroll_Y_5 == 1:
            fly_block5.rect.y-=5
            if fly_block5.rect.y < 50:
                scroll_Y_5  = 2
        elif scroll_Y_5 == 2:
            fly_block5.rect.y+=5
            if fly_block5.rect.y > 450:
                scroll_Y_5 = 1
        if hero_play_4.rect.x > 600 and hero_play_4.rect.y == 0:
            change = 8

        if sprite.collide_rect(hero_play_4,exit2):
            hero_play_4.rect.x = 0
            hero_play_4.rect.y = 380
            hero_play_4.speed_x = 0
            hero_play_4.speed_y = 0
            change = 0
    
    if change == 8:
        window.blit(phon_L5,(0,0))
        music_L.draw()
        M_L = music_L.draw()
        laserGood.reset()
        laserGood_basis.reset()
        laserBad.moving()
        laserGood_lift.reset()
        space_stone.reset()
        hero_play_5.moving()
        hero_play_5.update()

        bariers.remove(grass)
        bariers.remove(grass_block)
        bariers.remove(grass_block2)
        bariers.remove(cub1)
        bariers.remove(cub2)
        bariers.remove(cub3)
        bariers.remove(cub4)
        bariers.remove(cub5)
        bariers.remove(basis_spikes)
        bariers.remove(lift_X)
        bariers.remove(fly_block)
        bariers.remove(fly_block2)
        bariers.remove(fly_block3)
        bariers.remove(fly_block5)

        bariers.add(laserGood)
        bariers.add(laserGood_basis)
        bariers.add(laserGood_lift)
        bariers.add(space_stone)

        if scroll_Y_6 == 1:
            laserGood_lift.rect.x += 5
            if laserGood_lift.rect.x > 400:
                scroll_Y_6 = 2
        elif scroll_Y_6 == 2:
            laserGood_lift.rect.x -= 3
            if laserGood_lift.rect.x < 200:
                    scroll_Y_6 = 3
        elif scroll_Y_6 == 3:
            laserGood_lift.rect.x += 7
            if laserGood_lift.rect.x > 500:
                    scroll_Y_6 = 4
        elif scroll_Y_6 == 4:
            laserGood_lift.rect.y += 3
            if laserGood_lift.rect.y > 350:
                scroll_Y_6 = 5
        elif scroll_Y_6 == 5:
            laserGood_lift.rect.y -= 3
            if laserGood_lift.rect.y < 100:
                scroll_Y_6 = 6
        elif scroll_Y_6 == 6:
            laserGood_lift.rect.x -= 4
            if laserGood_lift.rect.x < 100:
                    scroll_Y_6 = 1

        if hero_play_5.rect.x > 50:
            laserBad.angle+=1

        if hero_play_5.rect.x < 20 and hero_play_5.rect.y < 50:
            change = 9 
            hero_play_5.rect.x = 0
            hero_play_5.rect.y = 400
            hero_play_5.speed_x = 0
            hero_play_5.speed_y = 0


        if sprite.collide_rect(hero_play_5,laserBad):
            hero_play_5.rect.x = 0
            hero_play_5.rect.y = 400
            hero_play_5.speed_x = 0
            hero_play_5.speed_y = 0
            change = 0
    if change == 0:
        window.blit(phon,(0,0))
        window.blit(final,(0,0))
        returnn.draw()
        R = returnn.draw()
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and R == False:
                change = 3
            elif e.type == QUIT:
                run = False

    if change == 9:
        window.blit(phon,(0,0))
        window.blit(phon_Win,(0,0))
        returnn.draw()
        R = returnn.draw()
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and R == False:
                change = 3
            elif e.type == QUIT:
                run = False

    display.update()
    clock.tick(60)
