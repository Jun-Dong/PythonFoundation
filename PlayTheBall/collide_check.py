import pygame
import sys
import math
from pygame.locals import *
from random import *


class Ball(pygame.sprite.Sprite):  # 球类继承Spirte类
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)  # 初始化动画精灵

        self.image = pygame.image.load(image).convert_alpha()  # 对于包含alpha通道的图片,使用convert alpha()转换格式,否则使用convert()
        self.rect = self.image.get_rect()  # 得到球的尺寸

        self.rect.left, self.rect.top = position  # 将小球放在指定位置,position:元组
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.right < 0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0:
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0


def collide_check(item, target):#sqrt开根
    col_balls = []
    for each in target:
        distance = math.sqrt(math.pow((item.rect.center[0] - each.rect.center[0]), 2) + math.pow((item.rect[1] - each.rect.center[1]), 2))
        if distance <= (item.rect.width + each.rect.width)/ 2:
            col_balls.append(each)
    return col_balls


def main():
    pygame.init()

    ball_image = 'gray_ball.png'
    bg_image = 'background.png'

    running = True
    bg_size = width, height = 1024, 681  # 根据背景图片指定游戏界面尺寸
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Play the ball')
    background = pygame.image.load(bg_image).convert_alpha()
    balls = []  # 用来存放小球对象的列表


    # 创建五个小球
    BALL_NUM = 5
    for i in range(BALL_NUM):
        # 位置随机,速度随机
        position = randint(0, width - 100), randint(0, height - 100)  # 球尺寸为100*100,以防球出界
        speed = [randint(-10, 10), randint(-10, 10)]  # x,y轴速度
        ball = Ball(ball_image, position, speed, bg_size)
        #测试诞生小球的位置是否存在其他的小球
        while collide_check(ball,balls):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        balls.append(ball)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)  # 更新图像

        for i in range(BALL_NUM):
            #先将要检测的小球取出来
            item = balls.pop(i)

            if collide_check(item,balls):
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]
            #将小球放回到列表中
            balls.insert(i,item)


        pygame.display.flip()  # 更新界面
        clock.tick(30)  # 设置每秒不高于30帧,用于控制游戏的速度


if __name__ == '__main__':
    main()
