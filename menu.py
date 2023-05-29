import pygame
from pac import *
from info import *
pygame.init()


WINDOW_WIDTH = 606
WINDOW_HEIGHT = 606
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load('background2.jpg').convert()
background_image = pygame.transform.scale(background_image, (1072,606))
pygame.display.set_caption("Pacman")
font2 = pygame.font.Font(cfg.FONTPATH, 20)   
text2 = font2.render("The goal of the game: collect all coins.", True, BLACK)
text3 = font2.render('Arrow control. Q - teleport forward for a short ',True,BLACK)
text4 = font2.render('distance (you can teleport between walls),',True,BLACK)
text5 = font2.render('player can teleport 3 times in a game.',True,BLACK)
text6 = font2.render('There are 2 teleports on the right and left side',True,BLACK)
text7 = font2.render('of map that can be used without restrictions.',True,BLACK)
text8 = font2.render('Also, a random number of cherries appear on the ',True,BLACK)
text9 = font2.render('field, picking which pacman gets invulnerability ',True,BLACK)
text10 = font2.render('to ghosts for a short period of time.',True,BLACK)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(cfg.FONTPATH, 36)
def draw_button():
    button_rect = pygame.Rect(253, 153, 102, 50)
    pygame.draw.rect(window, cfg.SKYBLUE, button_rect)
    text = font.render("PLAY!", True, BLACK)
    window.blit(text, (253,153))

    button1_rect = pygame.Rect(510, 10, 70, 40)
    pygame.draw.rect(window, cfg.SKYBLUE, button1_rect)
    text1 = font.render("Off", True, BLACK)
    window.blit(text1, (514,10))

    button2_rect = pygame.Rect(510, 60, 70, 40)
    pygame.draw.rect(window, cfg.SKYBLUE, button2_rect)
    text2 = font.render("On", True, BLACK)
    window.blit(text2, (520,60))
def draw_rect():
    rect = pygame.Rect(15, 348, 576, 200)
    pygame.draw.rect(window, cfg.SKYBLUE, rect)
def handle_button_click():
    main(initialize())
running = True
pygame.mixer.init()
pygame.mixer.music.load(cfg.BGMPATH)
pygame.mixer.music.play(-1, 0.0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(253, 153, 102, 50)
            button_rect2 = pygame.Rect(253, 253, 102, 50)
            button1_rect = pygame.Rect(510, 10, 70, 40)
            button2_rect = pygame.Rect(510, 60, 70, 40)
            if button_rect.collidepoint(mouse_pos):
                handle_button_click()
            elif button_rect2.collidepoint(mouse_pos):
                info()
            elif button1_rect.collidepoint(mouse_pos):
                pygame.mixer.music.pause()
            elif button2_rect.collidepoint(mouse_pos):
                pygame.mixer.music.unpause()
  
    window.blit(background_image, (0, 0))
    draw_rect()
    window.blit(text2,( 20, 353))
    window.blit(text3,( 20, 373))
    window.blit(text4,( 20, 393))
    window.blit(text5,( 20, 413))
    window.blit(text6,( 20, 433))
    window.blit(text7,( 20, 453))
    window.blit(text8,( 20, 473))
    window.blit(text9,( 20, 493))
    window.blit(text10,( 20, 513))
    draw_button()
    
    pygame.display.update()

pygame.quit()
