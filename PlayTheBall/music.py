import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()  # 初始化混音器模块

# 加载背景音乐:music
pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.2)  # 设置音量
pygame.mixer.music.play()

# 加载音效:Sound
cat_sound = pygame.mixer.Sound('loser.wav')
cat_sound.set_volume(0.2)  # 设置音量
dog_sound = pygame.mixer.Sound('laugh.wav')
dog_sound.set_volume(0.2)  # 设置音量
bg_size = width, height = 700, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Music - FishC.com')
pause = False
pause_image = pygame.image.load('hand.png').convert_alpha()
unpause_image = pygame.image.load('glass.png').convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            if event.button == 3:
                dog_sound.play()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause
    screen.fill((255,255,255))
    if pause:
        screen.blit(pause_image,pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image,pause_rect)

    pygame.display.flip()
    clock.tick(50)