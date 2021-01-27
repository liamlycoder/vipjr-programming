import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()


class MainWindow(object):
    def __init__(self, w, h):
        root.title("窗口")
        root.minsize(w, h)
        size = "{}x{}+{}+{}".format(w, h, 100, 200)
        root.geometry(size)

        self.btn = tk.Button(root)
        self.btn['text'] = "点我"
        self.btn.pack()

        self.btn.bind("<Button-1>", self.event)

    def show(self):
        root.mainloop()

    def event(self, e):
        messagebox.showinfo("Message", "欢迎来到tkinter")

    def addComponents(self):
        self.menubar = tk.Menu(root)
        root.configure(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label='游戏', menu=self.file_menu)
        self.menubar.add_cascade(label='编辑', menu=self.edit_menu)
        self.file_menu.add_command(label='新游戏', command=self.file_new)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='打开', command=self.open_file)
        self.file_menu.add_command(label='关闭', command=lambda: print("文件已关闭"))
        self.file_menu.add_command(label='保存', command=lambda: print("文件已保存"))
        self.edit_menu.add_command(label='粘贴', command=lambda: print('已粘贴'))
        self.edit_menu.add_command(label='复制', command=lambda: print('已复制'))

    def file_new(self):
        print(1)

    def open_file(self):
        input_file = filedialog.askopenfile(filetypes=[("所有文件", "*.*"), ("文本文档", "*.txt")])


game = MainWindow(400, 300)
game.addComponents()
game.show()
