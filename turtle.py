import pygame
import sys
from pygame.locals import *  # 引入所有常量名

pygame.init()
size = width, height = 600, 400
speed = [-2, 1]  # 移动的距离
bg = (255, 255, 255)  # 背景色(白色)
print(type(bg))

clock = pygame.time.Clock()  # 实例化Clock对象

fullscreen = False

screen = pygame.display.set_mode(size)  # 创建指定大小的窗体
print(type(screen))

pygame.display.set_caption('设置窗体标题')
turtle = pygame.image.load('turtle.jpg')
print(type(turtle))
position = turtle.get_rect()
print(type(position))

l_head = turtle  # 龟头朝左
r_head = pygame.transform.flip(turtle, True, False)  # 龟头朝右

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
                turtle = l_head
            if event.key == K_RIGHT:
                speed = [1, 0]
                turtle = r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]

            # 全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen == True:
                    screen = pygame.display.set_mode((1920, 1080), \
                                                     FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)

    position = position.move(speed)  # 不断移动
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)  # 水平翻转图像
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, position)  # 更新图像
    pygame.display.flip()  # 更新界面
    pygame.time.delay(10)  # 延迟10毫秒
    clock.tick(200)  # 设置不高于200帧执行
