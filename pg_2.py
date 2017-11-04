import pygame
import sys

pygame.init()
size = width,height = 600,400
bg = (0,0,0)#背景色(白色)
print(type(bg))
screen = pygame.display.set_mode(size)#创建指定大小的窗体
event_texts = []

#要在Pygame中使用文本必须创建一个Font对象
#参1:字体 2:尺寸
font = pygame.font.Font(None,20)
#调用get_linesize()方法获得每行文本高度
line_height = font.get_linesize()
position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(font.render(str(event),True,(0,255,0)),(0,position))#更新图像
    position += line_height
        #满屏时清屏
    if position > height:
        position = 0
        screen.fill(bg)
    
    pygame.display.flip() #更新界面
