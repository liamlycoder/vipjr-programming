# !/usr/bin/python
# coding: utf8
# Time: 2020/1/18 21:06
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import pygame
from pygame.locals import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("飞机大战")
        plane_img = pygame.image.load("resources/image/shoot.png")
        self.player = Player(plane_img, [200, 600])

    def show(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.player.drawPlane(self.screen)
            pygame.display.update()
            self.checkPressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

    def checkPressed(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.player.moveUp()
        if key_pressed[K_DOWN]:
            self.player.mvoeDown()
        if key_pressed[K_LEFT]:
            self.player.moveLeft()
        if key_pressed[K_RIGHT]:
            self.player.moveRight()


class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        player_rect = []
        player_rect.append(pygame.Rect(0, 99, 102, 126))
        player_rect.append(pygame.Rect(165, 360, 102, 126))
        self.image = []
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player_rect[0]
        self.img_index = 0
        self.temp = 0
        self.rect.topleft = init_pos
        self.speed = 8

    def moveUp(self):
        self.rect.top -= self.speed

    def mvoeDown(self):
        self.rect.top += self.speed

    def moveRight(self):
        self.rect.left += self.speed

    def moveLeft(self):
        self.rect.left -= self.speed

    def drawPlane(self, scr):
        self.temp += 1
        if self.temp >= 2:
            self.temp = 0
        scr.blit(self.image[self.img_index], self.rect)
        self.img_index = self.temp % 2


if __name__ == '__main__':
    game = MainWindow()
    game.show()
