import pygame
from pygame.locals import *
import random
from time import sleep

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("飞机大战")
        plane_img = pygame.image.load("resources/image/shoot.png")  # 整张图
        """新增7"""
        self.game_over = pygame.image.load('resources/image/gameover.png')
        self.player = Player(plane_img, [200, 600])

        self.enemies = pygame.sprite.Group()
        self.enemy_rect = pygame.Rect(534, 612, 57, 43)
        self.enemy_img = plane_img.subsurface(self.enemy_rect)

        self.enemies_down = pygame.sprite.Group()
        self.enemy_down_imgs = []
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
        self.enemy_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

        """新增5"""
        self.running = True


    def createEnemy(self, frequency):
        if frequency % 500 == 0:
            self.enemy_pos = [random.randint(0, SCREEN_WIDTH - self.enemy_rect.width), 0]
            self.enemy = Enemy(self.enemy_img, self.enemy_down_imgs, self.enemy_pos)
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
                """新增6"""
            # 判断玩家是否被击中
            if pygame.sprite.collide_circle(enemy, self.player):
                self.enemies_down.add(enemy)
                self.enemies.remove(enemy)
                self.player.is_hit = True
                self.running = False
                break

    def show(self):
        shoot_frequency = 0
        enemy_frequency = 0
        """新增"""
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.fill((255, 255, 255))
            self.player.drawPlane(self.screen)
            # self.screen.blit(self.enemy_down_imgs[3], (0, 0))
            shoot_frequency = self.checkPressed(shoot_frequency)
            self.player.moveBullet()
            self.player.drawBullets(self.screen)

            enemy_frequency = self.createEnemy(enemy_frequency)
            self.moveEnemy()
            self.enemies.draw(self.screen)

            self.judgeEnemy()

            pygame.display.update()
        """新增"""
        self.screen.blit(self.game_over, (0, 0))
        while True:
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == QUIT:
                    exit()


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

    def judgeEnemy(self):
        # 将被击中的敌机对象添加到击毁敌机Group中，用来渲染击毁动画
        down_dic = pygame.sprite.groupcollide(self.enemies, self.player.bullets, True, True)
        for enemy_down in down_dic:
            self.enemies_down.add(enemy_down)
        # 绘制敌机击毁动画
        for enemy_down in self.enemies_down:
            enemy_down.drawImg(self.screen)
            self.enemies_down.remove(enemy_down)


class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        super(Player, self).__init__()
        player_rect = []  # 存储两张玩家图的尺寸
        player_rect.append(pygame.Rect(5, 99, 98, 126))
        player_rect.append(pygame.Rect(170, 360, 98, 126))
        """新增1"""
        # 玩家爆炸精灵图片区域
        player_rect.append(pygame.Rect(165, 234, 102, 126))
        player_rect.append(pygame.Rect(330, 624, 102, 126))
        player_rect.append(pygame.Rect(432, 624, 102, 126))
        player_rect.append(pygame.Rect(330, 498, 102, 126))
        self.image = []  # 存储切好的两张玩家图
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]))
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.speed = 1
        self.img_index = 0  # 玩家图的索引

        """新增2"""
        self.is_hit = False


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

    """新增4"""
    def drawPlane(self, scr):
        self.img_index += 1
        if self.img_index >= 2:
            self.img_index = 0
        if self.is_hit:
            for i in range(2, 6):
                scr.blit(self.image[i], self.rect)
                pygame.display.update()
                print(i)
                sleep(0.02)
        else:
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = enemy_img.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1
        self.down_imgs = enemy_down_imgs

    def drawImg(self, scr):
        for i in range(4):
            scr.blit(self.down_imgs[i], self.rect)
            sleep(0.02)
            pygame.display.update()

    def move(self):
        self.rect.top += self.speed



if __name__ == '__main__':
    game = MainWindow()
    game.show()


