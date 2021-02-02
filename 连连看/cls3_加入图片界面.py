import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()


class MainWindow(object):
    __gameTitle = "连连看游戏"
    __windowWidth = 700
    __windowHeigth = 500
    __icons = []
    __gameSize = 10  # 游戏尺寸
    __iconKind = __gameSize * __gameSize / 4  # 小图片种类数量
    __iconWidth = 40
    __iconHeight = 40

    def __init__(self):
        root.title(self.__gameTitle)
        self.centerWindow(self.__windowWidth, self.__windowHeigth)
        root.minsize(460, 460)

        self.__addComponets()
        self.extractSmallIconList()

    def centerWindow(self, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def __addComponets(self):
        self.menubar = tk.Menu(root, bg="lightgrey", fg="black")

        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="新游戏", command=self.file_new, accelerator="Ctrl+N")

        self.menubar.add_cascade(label="游戏", menu=self.file_menu)
        root.configure(menu=self.menubar)

        self.canvas = tk.Canvas(root, bg='orange', width=450, height=450)
        self.canvas.pack(side=tk.TOP, pady=5)

    def file_new(self, event=None):
        self.drawMap()
        print('新游戏')

    def extractSmallIconList(self):
        imageSouce = Image.open('images/NARUTO.png')
        for index in range(0, int(self.__iconKind)):
            region = imageSouce.crop((self.__iconWidth * index, 0,
                                      self.__iconWidth * index + self.__iconWidth - 1, self.__iconHeight - 1))
            self.__icons.append(ImageTk.PhotoImage(region))
        print(self.__icons)

    def drawMap(self):
        self.canvas.delete("all")
        im = self.canvas.create_image(0, 0, image=self.__icons[1], anchor='nw')


game = MainWindow()
root.mainloop()
