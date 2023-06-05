
import pygame
from treba import *


window=pygame.display.set_mode((win_wid,win_hei))
pygame.display.set_caption(caption)
picture=pygame.transform.scale(pygame.image.load(display_picture),(win_wid,win_hei))



pygame.mixer.init()
over=pygame.mixer.Sound(defeat)
shot=pygame.mixer.Sound(fire)

bullets=pygame.sprite.Group()
enemy_fireballs=pygame.sprite.Group()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,name):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load(name),(width,height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,x,y,width,height,x_speed,y_speed,name,orien,walls_lvl,gates_lvl):
        GameSprite.__init__(self,x,y,width,height,name)
        self.x_speed=x_speed
        self.y_speed=y_speed
        self.orien=orien
        self.walls=walls_lvl
        self.gates=gates_lvl
    def update(self):

        if ghost.rect.x <= win_wid-50 and ghost.x_speed > 0 or ghost.rect.x >= 0 and ghost.x_speed < 0:
            self.rect.x += self.x_speed


        touched1 = pygame.sprite.spritecollide(self, self.walls, False)
        touched2 = pygame.sprite.spritecollide(self, self.gates, False)
        
        if self.x_speed > 0:
            for p in touched1:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in touched1:
                self.rect.left = max(self.rect.left, p.rect.right)
        
        if self.x_speed > 0:
            for p in touched2:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in touched2:
                self.rect.left = max(self.rect.left, p.rect.right)


        if ghost.rect.y <= win_hei-50 and ghost.y_speed > 0 or ghost.rect.y >= 0 and ghost.y_speed < 0:
            self.rect.y += self.y_speed
        



        touched1 = pygame.sprite.spritecollide(self, self.walls, False)
        touched2 = pygame.sprite.spritecollide(self, self.gates, False)
        if self.y_speed > 0:
            for p in touched1:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in touched1:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in touched2:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

        if self.y_speed > 0:
            for p in touched2:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in touched2:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in touched2:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

    




    
    def draw(self):
        if self.orien=='right':
            window.blit(self.image,(self.rect.x,self.rect.y))
        elif self.orien=='left':
            window.blit(pygame.transform.flip(self.image,True,False),(self.rect.x,self.rect.y))
    def fire(self):
        shot.play()
        if self.orien=='right':
            bullets.add(Bullet(self.rect.right, self.rect.centery, 15, 20, "bullet_right.png", 15))
        elif self.orien=='left':
            bullets.add(Bullet(self.rect.left, self.rect.centery, 15, 20, "bullet_left.png", -15))    

        
class EnemyX(GameSprite):
    def __init__(self,x,y,width,height,name,x1,x2,side,speed):
        GameSprite.__init__(self,x,y,width,height,name)
        self.start=x1
        self.end=x2
        self.speed=speed
        self.side=side
        self.health=7
    def update(self):

        if self.health<=0:
            self.kill()

        if self.rect.x <=self.start:
            self.side=ri
        elif self.rect.x >=self.end:
            self.side=le
        if self.side==le:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def fire(self):
        enemy_fireballs.add(Bullet(self.rect.left, self.rect.centery, 30, 20, "fireball.png", -15))

class EnemyY(GameSprite):
    def __init__(self,x,y,width,height,name,y1,y2,side,speed):
        GameSprite.__init__(self,x,y,width,height,name)
        self.start=y1
        self.end=y2
        self.speed=speed
        self.side=side
        self.health=7
    def update(self):

        if self.health<=0:
            self.kill()

        if self.rect.y <=self.start:
            self.side=ri
        elif self.rect.y >=self.end:
            self.side=le
        if self.side==le:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed





class Bullet(GameSprite):
    def __init__(self,x,y,width,height,name,speed):
        GameSprite.__init__(self,x,y,width,height,name)
        self.speed=speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_wid+10:
            self.kill()
        elif self.rect.x <0:
            self.kill()

class GameState():
    def __init__(self):
        

        self.state='level0'
        self.music=True
        
        
        self.finish_first_level = False
        self.finish_intermediate_level = False
        self.finish_second_level=False
        
        
        self.check_one=True
        self.check_two=True

        self.mage_killed=False
        self.key_get=False 

        self.firstbutton_touched=False
        self.secondbutton_touched=False

        self.fireball_cd=0
        self.wait_meter=0
    
    def level0(self):
        global play,intro_button
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play=False
            elif e.type==pygame.KEYDOWN:
                if e.key==pygame.K_SPACE:
                    self.state='level1'  
        window.blit(picture,(0,0))
        intro_button.draw()
          

    def level1(self):
        global final,ghost,walls_lvl1,demonsfirst,bullets,secretwall,holy_water,door_open,label1,finish,Spiritus_Bellator
        if self.music:
            pygame.mixer.music.load(main_music)
            pygame.mixer.music.play(-1)
            self.music=False
        Spiritus_Bellator.keyboard_bindings()    
        if not self.finish_first_level:  
            window.blit(picture,(0,0))
            final.draw()
            ghost.draw()
            walls_lvl1.draw(window)
            demonsfirst.draw(window)
            bullets.draw(window)
            secretwall.draw()
            bullets.update()
            demonsfirst.update()
            ghost.update()
            pygame.sprite.groupcollide(bullets,walls_lvl1,True,False)
            
            pygame.sprite.groupcollide(bullets,demonsfirst,True,True)

    
            if not door_open:
                        holy_water.draw()
                        if pygame.sprite.collide_rect(ghost, holy_water):
                            door_open=True
                            del holy_water


            if pygame.sprite.spritecollide(ghost, demonsfirst, False):
                pygame.mixer.music.stop()
                over.play()
                self.finish_first_level=True 
                img = pygame.image.load(lose)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))


            if pygame.sprite.collide_rect(ghost, final):
                if door_open==True:
                    self.finish_first_level=True
                    self.state='level1_1'
                else:
                    label1.draw()

    def level1_1(self):
        global walls_lvl1_1,ghost,Spiritus_Bellator,bullets,bigdemonsfirst,gates1_open,NPC,gate2,quote1,quote2,quote3,final1

        if self.check_one:
            ghost=Player(75,350,50,50,0,0,ghost_picture,ri,walls_lvl1_1,gates1_1)
            self.check_one=False
        Spiritus_Bellator.keyboard_bindings()
        if not self.finish_intermediate_level:
            window.blit(picture,(0,0))
            walls_lvl1_1.draw(window)
            bullets.draw(window)
            NPC.draw()
            ghost.draw()
            final1.draw()
            gates1_1.draw(window)
            bigdemonsfirst.draw(window)
            ghost.update()
            bullets.update()
            bigdemonsfirst.update()
            
            pygame.sprite.groupcollide(bullets,walls_lvl1_1,True,False)
            pygame.sprite.groupcollide(bullets,gates1_1,True,False)



            if pygame.sprite.collide_rect(ghost, NPC):
                self.key_get=True
                if self.wait_meter<25:
                    quote1.draw()
                    self.wait_meter+=0.1
                if self.wait_meter<50 and self.wait_meter>=25:
                    quote2.draw()
                    NPC.image=pygame.transform.scale(pygame.image.load("NPC_possesed2.png"),(60,75)) 
                    self.wait_meter+=0.1
                if self.wait_meter<100 and self.wait_meter>=50:
                    quote3.draw()
                    NPC.image=pygame.transform.scale(pygame.image.load("NPC_possesed3.png"),(60,75))
                    self.wait_meter+=0.5
                if self.wait_meter>=100:
                    over.play()
                    self.finish_intermediate_level=True
                    img = pygame.image.load(lose)
                    window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))

            demon_hit=pygame.sprite.groupcollide(bigdemonsfirst,bullets,False,True)
            for demon in demon_hit:
                demon.health-=1

            if pygame.sprite.spritecollide(ghost, bigdemonsfirst, False):
                pygame.mixer.music.stop()
                over.play()
                self.finish_intermediate_level=True
                img = pygame.image.load(lose)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))

            if len(bigdemonsfirst)==0:
                gates1_1.remove(firstgate)
            if self.key_get:
                gates1_1.remove(secondgate)
                    
            if pygame.sprite.collide_rect(ghost, final1):
                self.finish_intermediate_level=True
                self.state='level2'

    def level2(self):
        global walls_lvl2,gates2,ghost,Spiritus_Bellator,bullets,demonssecond,bigdemonssecond,final2,mage

        if self.check_two:
            ghost=Player(900,75,50,50,0,0,ghost_picture,le,walls_lvl2,gates2)
            self.check_two=False
        Spiritus_Bellator.keyboard_bindings() 
        if not self.finish_second_level:
            window.blit(picture,(0,0))
            firstbutton.draw()
            secondbutton.draw()
            ghost.draw()
            final2.draw()
            enemy_fireballs.draw(window)
            demonssecond.draw(window)
            bigdemonssecond.draw(window)
            walls_lvl2.draw(window)
            bullets.draw(window)
            gates2.draw(window)
            enemy_fireballs.update()
            demonssecond.update()
            bigdemonssecond.update()
            ghost.update()
            bullets.update()

            pygame.sprite.groupcollide(bullets,walls_lvl2,True,False)
            pygame.sprite.groupcollide(bullets,gates2,True,False)
            pygame.sprite.groupcollide(bullets,demonssecond,True,True)




            if not self.mage_killed:
                mage.draw()
                if pygame.sprite.spritecollide(mage,bullets,True):
                    self.mage_killed=True
                    del mage
                
                if self.fireball_cd<15:
                    self.fireball_cd+=0.5
                elif self.fireball_cd==15:
                    mage.fire()
                    self.fireball_cd=0


            if not self.firstbutton_touched:
                if pygame.sprite.collide_rect(ghost,firstbutton):
                    gates2.remove(thirdgate)
                    self.firstbutton_touched=True

            if not self.secondbutton_touched:
                if pygame.sprite.collide_rect(ghost,secondbutton):
                    gates2.remove(fifthgate)
                    self.secondbutton_touched=True
            
            if pygame.sprite.spritecollide(ghost,enemy_fireballs,False):
                pygame.mixer.music.stop()
                over.play()
                self.finish_second_level=True 
                img = pygame.image.load(lose)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))
            
            if pygame.sprite.spritecollide(ghost, demonssecond, False):
                pygame.mixer.music.stop()
                over.play()
                self.finish_second_level=True 
                img = pygame.image.load(lose)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))
            
            if pygame.sprite.spritecollide(ghost, bigdemonssecond, False):
                pygame.mixer.music.stop()
                over.play()
                self.finish_second_level=True
                img = pygame.image.load(lose)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))
                  
            demon_hit=pygame.sprite.groupcollide(bigdemonssecond,bullets,False,True)
            for demon in demon_hit:
                demon.health-=1

            if len(bigdemonssecond)==0:
                gates2.remove(fourthgate)
            
            if pygame.sprite.collide_rect(ghost, final2):
                pygame.mixer.music.stop()
                self.finish_second_level=True
                img = pygame.image.load(win)
                window.blit(pygame.transform.scale(img, (win_wid, win_hei)), (0, 0))


    def keyboard_bindings(self):
        global ghost,bulletsamount,play,bulletsamount,reloading
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play=False
            elif e.type==pygame.KEYDOWN:
                if e.key==pygame.K_LEFT or e.key==pygame.K_a:
                    ghost.x_speed=-7
                    ghost.orien=le
                elif e.key==pygame.K_RIGHT or e.key==pygame.K_d:
                    ghost.x_speed=7
                    ghost.orien=ri
                elif e.key==pygame.K_UP or e.key==pygame.K_w:
                    ghost.y_speed=-7
                elif e.key==pygame.K_DOWN or e.key==pygame.K_s:
                    ghost.y_speed=7
                elif e.key==pygame.K_SPACE:

                    if bulletsamount>0:
                        ghost.fire()
                        bulletsamount-=1

            elif e.type==pygame.KEYUP:
                if e.key==pygame.K_LEFT or e.key==pygame.K_a:
                    ghost.x_speed=0
                elif e.key==pygame.K_RIGHT or e.key==pygame.K_d:
                    ghost.x_speed=0
                elif e.key==pygame.K_UP or e.key==pygame.K_w:
                    ghost.y_speed=0
                elif e.key==pygame.K_DOWN or e.key==pygame.K_s:
                    ghost.y_speed=0
        
        if bulletsamount==0:
                reloading+=1
                if reloading>=35:
                    bulletsamount+=7
                    reloading=0

    def state_analyzer(self):
        if self.state=='level0':
            Spiritus_Bellator.level0()
        if self.state=='level1':
            Spiritus_Bellator.level1()
        if self.state=='level1_1':
            Spiritus_Bellator.level1_1()
        if self.state=='level2':
            Spiritus_Bellator.level2()





Spiritus_Bellator=GameState()

intro_button=GameSprite(win_wid/2-260,win_hei/2-55,520,220,button_start)

walls_lvl1=pygame.sprite.Group()
walls_lvl1.add(GameSprite(0,450,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(225,675,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(450,675,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(375,525,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(225,75,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(225,225,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(450,75,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(675,75,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(825,450,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(525,225,225,75,wall_horizontal))
walls_lvl1.add(GameSprite(225,375,75,225,wall_vertical))
walls_lvl1.add(GameSprite(675,300,75,225,wall_vertical))
walls_lvl1.add(GameSprite(375,300,75,225,wall_vertical))
walls_lvl1.add(GameSprite(525,300,75,225,wall_vertical))
walls_lvl1.add(GameSprite(150,75,75,225,wall_vertical))
walls_lvl1.add(GameSprite(825,150,75,225,wall_vertical))
secretwall=GameSprite(675,525,75,225,wall_vertical)


walls_lvl1_1=pygame.sprite.Group()
walls_lvl1_1.add(GameSprite(0,225,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(225,225,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(600,225,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(825,225,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(0,450,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(225,450,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(450,450,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(675,450,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(900,450,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(375,75,75,225,wall_vertical))
walls_lvl1_1.add(GameSprite(600,75,75,225,wall_vertical))
walls_lvl1_1.add(GameSprite(375,0,225,75,wall_horizontal))
walls_lvl1_1.add(GameSprite(450,0,225,75,wall_horizontal))


walls_lvl2=pygame.sprite.Group()
walls_lvl2.add(GameSprite(150,225,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(375,225,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(600,225,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(825,225,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(150,450,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(600,450,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(825,450,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(600,525,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(600,675,225,75,wall_horizontal))
walls_lvl2.add(GameSprite(150,265,75,225,wall_vertical))




gates1=pygame.sprite.Group()

firstgate=GameSprite(410.5,225,225,75,gates_hori)
secondgate=GameSprite(800,230,55,285,gates_verti)
gates1_1=pygame.sprite.Group()
gates1_1.add(firstgate)
gates1_1.add(secondgate)

thirdgate=GameSprite(150,0,75,225,gates_verti)
fourthgate=GameSprite(825,265,75,225,gates_verti)
fifthgate=GameSprite(375,450,225,75,gates_hori)
gates2=pygame.sprite.Group()
gates2.add(thirdgate)
gates2.add(fourthgate)
gates2.add(fifthgate)

firstbutton=GameSprite(250,80,60,60,button)
secondbutton=GameSprite(900,600,60,60,button)


NPC=GameSprite(495,100,60,75,npc_picture)

demonsfirst=pygame.sprite.Group()
demonsfirst.add(EnemyX(155,10,50,60,demon_picture,150,850,ri,5))
demonsfirst.add(EnemyX(230,160,50,60,demon_picture,225,775,ri,5))
demonsfirst.add(EnemyX(5,310,50,60,demon_picture,0,325,ri,5))

demonssecond=pygame.sprite.Group()
demonssecond.add(EnemyY(375,145,50,60,demon_picture,10,160,ri,5))
demonssecond.add(EnemyY(525,15,50,60,demon_picture,10,160,le,5))
demonssecond.add(EnemyY(675,145,50,60,demon_picture,10,160,ri,5))


bigdemonsfirst=pygame.sprite.Group()
bigdemonsfirst.add(EnemyX(674,300,100,150,big_demon,150,675,ri,12))

bigdemonssecond=pygame.sprite.Group()
bigdemonssecond.add(EnemyY(25,580,100,150,big_demon,10,580,le,12))
bigdemonssecond.add(EnemyX(650,300,100,150,big_demon,225,700,le,12))

mage=EnemyX(675,600,50,70,mage_picture,675,675,le,0)



ghost=Player(75,610,50,50,0,0,ghost_picture,ri,walls_lvl1,gates1)

final=GameSprite(900,600,75,75,door_picture)
final1=GameSprite(905,325,75,75,nice_door_picture)
final2=GameSprite(937.5,337.5,75,75,nice_door_picture)

holy_water=GameSprite(465,380,50,50,water_picture)
label1=GameSprite(350,650,400,100,text_picture)
quote1=GameSprite(350,650,400,100,npc_quote1)
quote2=GameSprite(350,650,400,100,npc_quote2)
quote3=GameSprite(350,650,400,100,npc_quote3)





while play: 
    Spiritus_Bellator.state_analyzer()
    
    pygame.time.delay(15)
    pygame.display.update()
