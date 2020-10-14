import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


"""
初始版本，敌军非常密集
    def createEnemy(self):
        self.enemy_pos = [random.randint(0, SCREEN_WIDTH - self.enemy_rect.width), 0]
        self.enemy = Enemy(self.enemy_img, self.enemy_pos)
        self.enemies.add(self.enemy)

    def moveEnemy(self):
        for enemy in self.enemies:
            enemy.move()
            if enemy.rect.top > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
"""


class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("飞机大战")
        plane_img = pygame.image.load("resources/image/shoot.png")  # 整张图
        self.player = Player(plane_img, [200, 600])

        # 新增内容2
        self.enemies = pygame.sprite.Group()
        self.enemy_rect = pygame.Rect(534, 612, 57, 43)
        self.enemy_img = plane_img.subsurface(self.enemy_rect)


    def createEnemy(self, frequency):
        if frequency % 500 == 0:
            self.enemy_pos = [random.randint(0, SCREEN_WIDTH - self.enemy_rect.width), 0]
            self.enemy = Enemy(self.enemy_img, self.enemy_pos)
            self.enemies.add(self.enemy)
        frequency += 1
        if frequency >= 500:
            frequency = 0
        return frequency

    def moveEnemy(self):
        for enemy in self.enemies:
            enemy.move()
            if enemy.rect.top > SCREEN_HEIGHT:
                self.enemies.remove(enemy)

    def show(self):
        shoot_frequency = 0
        enemy_frequency = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.fill((255, 255, 255))
            self.player.drawPlane(self.screen)
            shoot_frequency = self.checkPressed(shoot_frequency)
            self.player.moveBullet()
            self.player.drawBullets(self.screen)

            enemy_frequency = self.createEnemy(enemy_frequency)
            self.moveEnemy()
            self.enemies.draw(self.screen)


            pygame.display.update()


    def checkPressed(self, frequency):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.player.moveUp()
        if key_pressed[K_DOWN]:
            self.player.moveDown()
        if key_pressed[K_LEFT]:
            self.player.moveLeft()
        if key_pressed[K_RIGHT]:
            self.player.moveRight()
        if key_pressed[K_SPACE]:
            if frequency % 40 == 0:
                self.player.shoot()
            frequency += 1
            if frequency >= 40:
                frequency = 0
        return frequency


class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        player_rect = []  # 存储两张玩家图的尺寸
        player_rect.append(pygame.Rect(5, 99, 98, 126))
        player_rect.append(pygame.Rect(170, 360, 98, 126))
        self.image = []  # 存储切好的两张玩家图
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]))
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.speed = 1
        self.img_index = 0  # 玩家图的索引

        # 把图片中子弹部分剪下来
        self.bullets = pygame.sprite.Group()
        bullets_rect = pygame.Rect([1004, 987, 9, 21])
        self.bullet_image = plane_img.subsurface(bullets_rect)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

    def drawPlane(self, scr):
        self.img_index += 1
        if self.img_index >= 2:
            self.img_index = 0
        scr.blit(self.image[self.img_index], self.rect)

    def shoot(self):
        bullet = Bullet(self.bullet_image, self.rect.midtop)
        self.bullets.add(bullet)

    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):  # 需要传入子弹的图片和初始位置
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img  # 图片变为成员变量
        self.rect = bullet_img.get_rect()   # 获取图片尺寸
        self.rect.midbottom = init_pos  # 设置初始位置
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed


# 新增内容1
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = enemy_img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1

    def move(self):
        self.rect.top += self.speed



if __name__ == '__main__':
    game = MainWindow()
    game.show()


