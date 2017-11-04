import pygame
import sys
from pygame.locals import *
from random import *


class Ball(pygame.sprite.Sprite):  # 球类继承Spirte类
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)  # 初始化动画精灵

        self.grayball_image = pygame.image.load(
            grayball_image).convert_alpha()  # 对于包含alpha通道的图片,使用convert alpha()转换格式,否则使用convert()
        self.greenball_image = pygame.image.load(
            greenball_image).convert_alpha()  # 对于包含alpha通道的图片,使用convert alpha()转换格式,否则使用convert()
        self.rect = self.grayball_image.get_rect()  # 得到球的尺寸
        self.rect.left, self.rect.top = position  # 将小球放在指定位置,position:元组
        self.side = [choice([-1, 1]), choice([-1, 1])]
        self.speed = speed
        self.target = target
        self.control = False
        self.collide = False
        self.radius = self.rect.width / 2

        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move((self.side[0] * self.speed[0],
                                    self.side[1] * self.speed[1]))

        # 如果小球的左侧除了边界,那么将小球左侧的位置改为右侧的边界
        # 这样便实现了从左边进入,右边除了的效果
        if self.rect.right < 0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0:
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0

    def check(self, motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False


class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) // 2, \
                                                    bg_size[1] - self.glass_rect.height

        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top
        # 初始化鼠标的位置位于左上角
        # pygame.mouse.set_pos([self.glass_rect.left,self.glass_rect.top])
        # 鼠标不可见
        pygame.mouse.set_visible(False)


def main():
    pygame.init()
    grayball_image = 'gray_ball.png'
    greenball_image = 'green_ball.png'
    bg_image = 'background.png'
    mouse_image = 'hand.png'
    glass_image = 'glass.png'
    running = True
    # 添加魔性音乐
    pygame.mixer.music.load("bg_music.ogg")
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play()

    loser_sound = pygame.mixer.Sound('loser.wav')
    laugh_sound = pygame.mixer.Sound('laugh.wav')
    winner_sound = pygame.mixer.Sound('winner.wav')
    hole_sound = pygame.mixer.Sound('hole.wav')

    # 自定义事件
    # 音乐放完时游戏结束!
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)

    bg_size = width, height = 1024, 681  # 根据背景图片指定游戏界面尺寸
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Play the ball')
    background = pygame.image.load(bg_image).convert_alpha()

    # 5 个坑的范围，因为 100% 命中太难，所以只要在范围内即可
    # 每个元素：(x1, x2, y1, y2)

    hole = [(117, 122, 199, 204), (225, 230, 390, 395), \
            (503, 508, 320, 325), (698, 703, 192, 197), \
            (906, 911, 419, 425)]
    msgs = []
    # 用来存放小球对象的列表
    balls = []
    group = pygame.sprite.Group()  # 第二个参数:指定一个组

    # 创建五个小球
    BALL_NUM = 5
    for i in range(5):
        # 位置随机,速度随机
        position = randint(0, width - 100), randint(0, height - 100)  # 球尺寸为100*100,以防球出界
        speed = [randint(1, 10), randint(1, 10)]  # x,y轴速度:都为正数
        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i + 1))

        # 检测新诞生的球是否会卡住其他球
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)

        balls.append(ball)
        group.add(ball)

    glass = Glass(glass_image, mouse_image, bg_size)
    # motion 用于记录鼠标在玻璃面板产生的事件数量
    motion = 0
    # 一秒检查一次摩擦摩擦
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000)

    pygame.key.set_repeat(100, 100)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                running = False

            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0
            elif event.type == MOUSEMOTION:
                motion += 1

                # 当小球的 control 属性为 True 时
                # 可是使用按键 w、s、a、d 分别上、下、左、右移动小球
                # 带加速度的哦^_^
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1

                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1

                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1

                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0] <= each.rect.left <= i[1] and\
                                    i[2] <= each.rect.top <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0,0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0,temp)
                                    hole.remove(i)
                                if not hole:
                                    pygame.mixer.music.stop()
                                    winner_sound.play()
                                    pygame.time.delay(3000)
                                    msg = pygame.image.load('win.png').convert_apha()
                                    msg_pos = (width - msg.get_width())//2,
                                    (height - msg.get_height())//2
                                    msgs.append((msg,msg_pos))
                                    laugh_sound.play()

        screen.blit(background, (0, 0))
        screen.blit(glass.glass_image, glass.glass_rect)

        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height

        screen.blit(glass.mouse_image, glass.mouse_rect)

        for each in balls:
            each.move()
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False

            # 被控制画成绿色小球
            if each.control:
                screen.blit(each.greenball_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)

        for each in group:
            # 先从组里移除当前球
            group.remove(each)
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False#碰撞后变回灰色

            # 将当前球添加回组中
            group.add(each)

        for msg in msgs:
            screen.blit(msg[0],msg[1])

        pygame.display.flip()  # 更新界面
        clock.tick(70)  # 设置每秒不高于30帧,用于控制游戏的速度


if __name__ == '__main__':
    main()
