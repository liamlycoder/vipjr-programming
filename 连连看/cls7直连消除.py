import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


class MainWindow(object):
    __gameTitle = "连连看游戏"
    __windowWidth = 700
    __windowHeigth = 500
    __icons = []
    __gameSize = 10  # 游戏尺寸
    __iconKind = 25  # 小图片种类数量
    __iconWidth = 40
    __iconHeight = 40
    __map = []  # 游戏地图
    __delta = 25

    EMPTY = -1
    __isGameStart = False

    __isFirst = True
    __formerPoint = None

    """新增代码1"""
    NONE_LINK = 0  # 无连接
    STRAIGHT_LINK = 1  # 直连
    ONE_CORNER_LINK = 2  # 一拐
    TWO_CORNER_LINK = 3  # 两拐

    def __init__(self):
        root.title(self.__gameTitle)
        self.centerWindow(self.__windowWidth, self.__windowHeigth)
        root.minsize(460, 460)

        self.__addComponets()
        self.extractSmallIconList()

    def __addComponets(self):
        self.menubar = tk.Menu(root, bg="lightgrey", fg="black")

        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="新游戏", command=self.file_new, accelerator="Ctrl+N")

        self.menubar.add_cascade(label="游戏", menu=self.file_menu)
        root.configure(menu=self.menubar)

        self.canvas = tk.Canvas(root, bg='gold', width=450, height=450)
        self.canvas.pack(side=tk.TOP, pady=5)
        self.canvas.bind("<Button-1>", self.clickCanvas)

    def clickCanvas(self, event):
        if self.__isGameStart:
            indexPoint = self.getInnerPoint(Point(event.x, event.y))
            if indexPoint.isUserful() and not self.isEmptyInMap(indexPoint):
                if self.__isFirst:
                    self.drawSelectedArea(indexPoint)
                    self.__isFirst = False
                    self.__formerPoint = indexPoint
                else:
                    if self.__formerPoint.isEqual(indexPoint):
                        self.__isFirst = True
                        self.canvas.delete("rectRedOne")
                    else:
                        """新增代码5：更改逻辑"""
                        linkType = self.getLinkType(self.__formerPoint, indexPoint)
                        if linkType['type'] != self.NONE_LINK:
                            # TODO Animation
                            self.ClearLinkedBlocks(self.__formerPoint, indexPoint)
                            self.canvas.delete("rectRedOne")
                            self.__isFirst = True
                        else:
                            self.__formerPoint = indexPoint
                            self.canvas.delete("rectRedOne")
                            self.drawSelectedArea(indexPoint)

    def centerWindow(self, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def file_new(self, event=None):
        self.iniMap()
        self.drawMap()
        self.__isGameStart = True

    '''
    提取小头像数组
    '''

    def extractSmallIconList(self):
        imageSouce = Image.open('images/NARUTO.png')
        for index in range(0, self.__iconKind):
            region = imageSouce.crop((self.__iconWidth * index, 0,
                                      self.__iconWidth * index + self.__iconWidth, self.__iconHeight))
            self.__icons.append(ImageTk.PhotoImage(region))

    '''
    初始化地图 存值为0-24
    '''

    def iniMap(self):
        self.__map = []  # 重置地图
        records = []
        for i in range(0, self.__iconKind):
            for j in range(0, 4):
                records.append(i)

        random.shuffle(records)

        # 一维数组转为二维，y为高维度
        for y in range(0, self.__gameSize):
            for x in range(0, self.__gameSize):
                if x == 0:
                    self.__map.append([])
                self.__map[y].append(records[x + y * self.__gameSize])

    '''
    根据地图绘制图像
    '''

    def drawMap(self):
        self.canvas.delete("all")
        for y in range(0, self.__gameSize):
            for x in range(0, self.__gameSize):
                point = self.getOuterLeftTopPoint(Point(x, y))
                im = self.canvas.create_image((point.x, point.y),
                                              image=self.__icons[self.__map[y][x]], anchor='nw', tags='im%d%d' % (x, y))

    '''
    获取内部坐标对应矩形左上角顶点坐标
    '''

    def getOuterLeftTopPoint(self, point):
        return Point(self.getX(point.x), self.getY(point.y))


    def drawSelectedArea(self, point):
        pointLT = self.getOuterLeftTopPoint(point)
        pointRB = self.getOuterLeftTopPoint(Point(point.x + 1, point.y + 1))
        self.canvas.create_rectangle(pointLT.x, pointLT.y,
                                     pointRB.x - 1, pointRB.y - 1, outline='red', tags="rectRedOne")

    def getX(self, x):
        return x * self.__iconWidth + self.__delta

    def getY(self, y):
        return y * self.__iconHeight + self.__delta

    '''
    获取内部坐标
    '''
    def getInnerPoint(self, point):
        x = -1
        y = -1

        for i in range(0, self.__gameSize):
            x1 = self.getX(i)
            x2 = self.getX(i + 1)
            if x1 <= point.x < x2:
                x = i

        for j in range(0, self.__gameSize):
            j1 = self.getY(j)
            j2 = self.getY(j + 1)
            if j1 <= point.y < j2:
                y = j

        return Point(x, y)

    '''
    地图上该点是否为空
    '''
    def isEmptyInMap(self, point):
        return self.__map[point.y][point.x] == self.EMPTY

    '''
    新增代码2：获取两个点连通类型
    '''

    def getLinkType(self, p1, p2):
        # 首先判断两个方块中图片是否相同
        if self.__map[p1.y][p1.x] != self.__map[p2.y][p2.x]:
            return {'type': self.NONE_LINK}

        if self.isStraightLink(p1, p2):
            return {
                'type': self.STRAIGHT_LINK
            }

    '''
    新增代码3：直连
    '''

    def isStraightLink(self, p1, p2):
        start = -1
        end = -1
        # 水平
        if p1.y == p2.y:
            # 大小判断
            if p2.x < p1.x:
                start = p2.x
                end = p1.x
            else:
                start = p1.x
                end = p2.x
            for x in range(start + 1, end):
                if self.__map[p1.y][x] != self.EMPTY:
                    return False
            return True
        elif p1.x == p2.x:
            if p1.y > p2.y:
                start = p2.y
                end = p1.y
            else:
                start = p1.y
                end = p2.y
            for y in range(start + 1, end):
                if self.__map[y][p1.x] != self.EMPTY:
                    return False
            return True
        return False

    '''
    新增代码4：消除连通的两个块
    '''
    def ClearLinkedBlocks(self, p1, p2):
        self.__map[p1.y][p1.x] = self.EMPTY
        self.__map[p2.y][p2.x] = self.EMPTY
        self.canvas.delete('im%d%d' % (p1.x, p1.y))
        self.canvas.delete('im%d%d' % (p2.x, p2.y))


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isUserful(self):
        return self.x >= 0 and self.y >= 0


    def isEqual(self, point):
        return self.x == point.x and self.y == point.y


m = MainWindow()
root.mainloop()
