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
                print(indexPoint.x, indexPoint.y)

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


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isUserful(self):
        return self.x >= 0 and self.y >= 0


m = MainWindow()
root.mainloop()
