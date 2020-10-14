# !/usr/bin/python
# coding: utf8
# Time: 2020/1/18 22:27
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

    def show(self):
        while True:
            self.screen.fill((0, 0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()


if __name__ == '__main__':
    game = MainWindow()
    game.show()
