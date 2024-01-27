import pygame
import random
import sys
import math
import time
from datetime import datetime

pygame.init()

screen_x = 1550
screen_y = 1550

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("ᜋᜇᜒ ᜊ᜔ᜌ᜔ : ᜌᜐ᜔ᜑᜒᜃ᜔")

def File_Game_SpaceAttack():
    baclground_color_R = 0
    baclground_color_G = 0
    baclground_color_B = 0
    
    run_game = True
    
    def Background_fill(r, g, b):
        screen.fill((r, g, b))
    
    def text(*t, color, position, size):
        font = pygame.font.SysFont("Times New Roman", size)
        text_surface = font.render(" ".join(map(str, t)), True, (color[0], color[1], color[2]))
        screen.blit(text_surface, (position[0],position[1]))
    
    def display():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
    
    def hitbox(color=(0, 255, 0), position=(0, 0), size=(0, 0)):
        button_rect = pygame.Rect(position[0], position[1], size[0], size[1])
        pygame.draw.rect(screen, color, button_rect, hitbox_size)
        return button_rect
    
    def enemy_001_ui(x, y):
        pygame.draw.circle(screen, (180, 0, 0), (x, y), 25, 6)
        pygame.draw.circle(screen, (180, 0, 0), (x, y), 15)
        pygame.draw.polygon(screen, (180, 0, 0), ((x-25, y), (x-40, y), (x-25, y+50), ))
        pygame.draw.polygon(screen, (180, 0, 0), ((x+25, y), (x+40, y), (x+25, y+50), ))
    
    def player_ui(x,y, type):
        pygame.draw.circle(screen, (0, 220, 180), (x, y), 25, 6)
        pygame.draw.circle(screen, (0, 220, 180), (x, y), 15)
        if type == 1:
            pygame.draw.polygon(screen, (0, 220, 180), ((x-25,y+25), (x-40,y), (x-30,y-40), (x-15, y-50), (x-25, y-40)))
            pygame.draw.polygon(screen, (0, 220, 180), ((x+25,y+25), (x+40,y), (x+30,y-40), (x+15, y-50), (x+25, y-40)))
            pygame.draw.polygon(screen, (0, 220, 180), ((x+30,y+30), (x+43, y+10), (x+50, y+40)))
            pygame.draw.polygon(screen, (0, 220, 180), ((x-30,y+30), (x-43, y+10), (x-50, y+40)))
        if type == 2:
            pygame.draw.polygon(screen, (0, 220, 180), ((x-40,y+25), (x-40,y), (x-30,y-40), (x-25, y-70), (x-15, y-40)))
            pygame.draw.polygon(screen, (0, 220, 180), ((x+40,y+25), (x+40,y), (x+30,y-40), (x+25, y-70), (x+15, y-40)))
        if type == 3:
            pygame.draw.polygon(screen, (0, 220, 180), ((x-50,y+25), (x-40,y), (x-30,y-40), (x-30, y-70), (x-15, y-80), (x-20, y-65), (x-15, y-40)))
            pygame.draw.polygon(screen, (0, 220, 180), ((x+50,y+25), (x+40,y), (x+30,y-40), (x+30, y-70), (x+15, y-80), (x+20, y-65), (x+15, y-40)))
        
    while run_game:
        room_number = 0
        
        hitbox_size = 1
        
        #system
        score = 0
        high_score = 0
        damage_multiplier = 0
        
        move_item_001 = 0
        move_item_002 = 0
        
        #player
        player_health = 0
        
        player_bullets = 0
        player_bullets_loc = 0
        player_bullet_reload_speed = 4
        bullet_type = 1
        
        player_x_location = 0
        player_movement_speed = 10
        
        #enemy
        enemy_001_HP = 50
        enemy_001_DMG = 2
        enemy_001_RanChance = 0, 1500
        enemy_001_laser_size = 50
        
        enemy_002_HP = 150
        enemy_002_DMG = 5
        enemy_002_RanChance = 0, 3000
        enemy_001_laser_size = 75
        
        enemy_003_HP = 500
        enemy_003_DMG = 10
        enemy_003_RanChance = 750, 750
        enemy_001_laser_size = 125
        
        first_game = 0
        
        while run_game:
            if score > high_score:
                high_score = score
            if room_number == 0:
                Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100), size=90)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200), size=20)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                
                text("HIGH SCORE :", str(high_score), color=(210, 0, 0), position=(210, 300), size=40)
                
                player_ui(360,450, bullet_type)
                
                pygame.draw.rect(screen, (140, 0, 0), (210, 600, 300, 100), 5)
                text("START", color=(210, 0, 0), position=(270, 620), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 730, 300, 100), 5)
                text("TUTORIAL", color=(210, 0, 0), position=(225, 750), size=55)
                pygame.draw.rect(screen, (140, 0, 0), (210, 860, 300, 100), 5)
                text("CREDITS", color=(210, 0, 0), position=(235, 880), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 990, 300, 100), 5)
                text("EXIT", color=(210, 0, 0), position=(290, 1010), size=60)
                
                start_hitbox = hitbox(color=(0, 255, 0), position=(210, 600), size=(300, 100))
                tutorial_hitbox = hitbox(color=(0, 255, 0), position=(210, 730), size=(300, 100))
                credits_hitbox = hitbox(color=(0, 255, 0), position=(210, 860), size=(300, 100))
                exit_hitbox = hitbox(color=(0, 255, 0), position=(210, 990), size=(300, 100))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 3
                elif credits_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 2
                elif exit_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 1
                display()
                
            elif room_number == 1:
                Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100), size=90)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200), size=20)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                
                text("[ Are you sure you want to exit the game? ]", color=(210, 0, 0), position=(50, 300), size=30)
                
                pygame.draw.rect(screen, (140, 0, 0), (210, 600, 300, 100), 5)
                text("YES", color=(210, 0, 0), position=(310, 620), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 730, 300, 100), 5)
                text("NO", color=(210, 0, 0), position=(320, 750), size=60)
                
                yes_hitbox = hitbox(color=(0, 255, 0), position=(210, 600), size=(300, 100))
                no_hitbox = hitbox(color=(0, 255, 0), position=(210, 730), size=(300, 100))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if yes_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    run_game = False
                elif no_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 0
                display()
            
            elif room_number == 2:
                Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100), size=90)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200), size=20)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                
                text("[ Credits ]", color=(210, 0, 0), position=(270, 300), size=40)
                
                text("creator | Vallite", color=(210, 0, 0), position=(280, 390), size=20)
                text("art | Vallite", color=(210, 0, 0), position=(322, 410), size=20)
                text("design | Vallite", color=(210, 0, 0), position=(287, 430), size=20)
                text("music | N/A", color=(210, 0, 0), position=(294, 450), size=20)
                text("code | Vallite", color=(210, 0, 0), position=(306, 470), size=20)
                text("computer language | Python3", color=(210, 0, 0), position=(167, 490), size=20)
                text("IDE | Pydriod 3", color=(210, 0, 0), position=(314, 510), size=20)
                
                pygame.draw.rect(screen, (140, 0, 0), (210, 1350, 300, 100), 5)
                text("RETURN", color=(210, 0, 0), position=(240, 1370), size=60)
                
                return_hitbox = hitbox(color=(0, 255, 0), position=(210, 1350), size=(300, 100))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if return_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 0
                display()
            
            elif room_number == 3:
                Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100), size=90)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200), size=20)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                
                player_ui(360,450, bullet_type)
                
                pygame.draw.rect(screen, (140, 0, 0), (210, 600, 300, 100), 5)
                text("LEVEL 1", color=(210, 0, 0), position=(240, 620), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 730, 300, 100), 5)
                text("LEVEL 2", color=(210, 0, 0), position=(240, 750), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 860, 300, 100), 5)
                text("LEVEL 3", color=(210, 0, 0), position=(240, 880), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 990, 300, 100), 5)
                text("RETURN", color=(210, 0, 0), position=(240, 1010), size=60)
                
                level1_hitbox = hitbox(color=(0, 255, 0), position=(210, 600), size=(300, 100))
                level2_hitbox = hitbox(color=(0, 255, 0), position=(210, 730), size=(300, 100))
                level3_hitbox = hitbox(color=(0, 255, 0), position=(210, 860), size=(300, 100))
                return_hitbox = hitbox(color=(0, 255, 0), position=(210, 990), size=(300, 100))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if level1_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 4
                if level2_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 5
                elif return_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 0
                display()
            elif room_number == 4:
                #cutscene
                move_item_001 = 0
                move_item_002 = 0
                player_health = 100
                player_bullets = 0
                player_bullets += 1
                for i in range (25):
                    Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                    player_ui(360,450-move_item_002, bullet_type)
                    pygame.draw.rect(screen, (0,0,0), (0, 0-move_item_001, 720, 230))
                    text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100-move_item_001), size=90)
                    text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200-move_item_001), size=20)
                    text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85-move_item_001), size=20)
                    move_item_001 += 10
                    move_item_002 += 20
                    player_bullets += 1
                    display()
                for i in range (50):
                    Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                    pygame.draw.rect(screen, (210, 0, 0), (-5, 0-move_item_001, 730, 110), 3)
                    pygame.draw.rect(screen, (210, 0, 0), (-5, 0-move_item_001, 730, 86), 3)
                    pygame.draw.circle(screen, (80, 80, 80), (360, 50-move_item_001), 25, 5)
                    pygame.draw.circle(screen, (0, 255, 0), (360, 50-move_item_001), 20)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5-move_item_001, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 0, 0), (8, 8-move_item_001, player_health*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5-move_item_001, 206, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 28-move_item_001, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 255, 0), (8, 31-move_item_001, player_bullets*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (209, 28-move_item_001, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (209, 5-move_item_001, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (434, 5-move_item_001, 282, 52), 3)
                    text(str(player_health)+"/100", color=(255, 255, 255), position=(215, 6-move_item_001), size=18)
                    text(str(player_bullets)+"/100", color=(255, 255, 255), position=(215, 31-move_item_001), size=18)
                    text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85-move_item_001), size=20)
                    move_item_001 -= 5
                    player_bullets += 1
                    display()
                move_item_002 = 0
                for i in range (25):
                    Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                    
                    player_ui(360,1600+move_item_002, bullet_type)
                    
                    pygame.draw.rect(screen, (0,0,0), (0, 0, 720, 110))
                    pygame.draw.rect(screen, (210, 0, 0), (-5, -50, 730, 137), 3)
                    pygame.draw.rect(screen, (210, 0, 0), (-5, -5, 730, 113), 3)
                    pygame.draw.circle(screen, (80, 80, 80), (360, 50), 25, 5)
                    pygame.draw.circle(screen, (0, 255, 0), (360, 50), 20)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 0, 0), (8, 8, player_health*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5, 206, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 28, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 255, 0), (8, 31, player_bullets*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (209, 28, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (209, 5, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (434, 5, 282, 52), 3)
                    text(str(player_health)+"/100", color=(255, 255, 255), position=(215, 6), size=18)
                    text(str(player_bullets)+"/100", color=(255, 255, 255), position=(215, 31), size=18)
                    text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                    
                    player_bullets += 1
                    move_item_002 -= 10
                    display()
                while True:
                    Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                    
                    #player
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if first_game < 1:
                        pygame.mouse.set_pos(360, 360)
                        first_game += 1
                        
                    if mouse_x == player_x_location:
                        print('ok')
                    else:
                        if mouse_x > player_x_location:
                            player_x_location += player_movement_speed
                        if mouse_x < player_x_location:
                            player_x_location -= player_movement_speed
                    
                    if player_bullets > 100:
                        player_bullets = 0
                        player_bullets_loc = player_x_location
                        
                    #player_ui
                    if bullet_type == 1:
                        player_bullet_ui = pygame.draw.rect(screen, (255, 255, 0), (player_bullets_loc-10, 1320-player_bullets*20, 20, 20))
                    elif bullet_type == 2:
                        player_bullet_ui = pygame.draw.rect(screen, (255, 255, 0), (player_bullets_loc-5, 1220-player_bullets*20, 10, 100))
                    elif bullet_type == 3:
                        if player_bullets < 30:
                            player_bullet_ui = pygame.draw.rect(screen, (255, 255, 0), (player_bullets_loc-10, 1220-player_bullets*20, 20, 20))
                        elif player_bullets > 40:
                            pygame.draw.rect(screen, (255, 0, 0), (player_bullets_loc-50, 1220-player_bullets*20, 100, 100))
                    
                    player_ui(player_x_location,1360, bullet_type)
                    
                    pygame.draw.rect(screen, (0,0,0), (0, 0, 720, 110))
                    pygame.draw.rect(screen, (210, 0, 0), (-5, -50, 730, 137), 3)
                    pygame.draw.rect(screen, (210, 0, 0), (-5, -5, 730, 113), 3)
                    pygame.draw.circle(screen, (80, 80, 80), (360, 50), 25, 5)
                    pygame.draw.circle(screen, (0, 255, 0), (360, 50), 20)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 0, 0), (8, 8, player_health*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (5, 5, 206, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (5, 28, 206, 26), 3)
                    pygame.draw.rect(screen, (255, 255, 0), (8, 31, player_bullets*2, 20))
                    pygame.draw.rect(screen, (80, 80, 80), (209, 28, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (209, 5, 76, 26), 3)
                    pygame.draw.rect(screen, (80, 80, 80), (434, 5, 282, 52), 3)
                    text(str(player_health)+"/100", color=(255, 255, 255), position=(215, 6), size=18)
                    text(str(player_bullets)+"/100", color=(255, 255, 255), position=(215, 31), size=18)
                    text("p_loc :",str(player_x_location), "1360", color=(255, 255, 255), position=(440, 10), size=10)
                    text("m_loc :",str(mouse_x),str(mouse_y), color=(255, 255, 255), position=(440, 20), size=10)
                    text("b_loc :",str(player_bullets_loc),str(player_bullets), color=(255, 255, 255), position=(440, 30), size=10)
                    text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                    
                    player_bullets += player_bullet_reload_speed
                    move_item_002 -= 10
                    display()
            else:
                Background_fill(baclground_color_R, baclground_color_G, baclground_color_B)
                
                player_ui(360,450, bullet_type)
                
                text("SPACE ATTACK", color=(210, 0, 0), position=(40, 100), size=90)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 200), size=20)
                text("✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙✙", color=(180, 0, 0), position=(0, 85), size=20)
                
                text("[ ERROR # 404 - ROOM NOT FOUND ]", color=(210, 0, 0), position=(100, 300), size=30)
                
                pygame.draw.rect(screen, (140, 0, 0), (210, 600, 300, 100), 5)
                text("EXIT", color=(210, 0, 0), position=(290, 620), size=60)
                pygame.draw.rect(screen, (140, 0, 0), (210, 730, 300, 100), 5)
                text("RETURN", color=(210, 0, 0), position=(240, 750), size=60)
                
                exit_hitbox = hitbox(color=(0, 255, 0), position=(210, 600), size=(300, 100))
                return_hitbox = hitbox(color=(0, 255, 0), position=(210, 730), size=(300, 100))
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if exit_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 1
                elif return_hitbox.collidepoint(mouse_x, mouse_y):
                    pygame.mouse.set_pos(0, 0)
                    room_number = 0
                display()
            
File_Game_SpaceAttack()
