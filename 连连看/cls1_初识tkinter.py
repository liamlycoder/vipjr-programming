import tkinter as tk
from tkinter import messagebox

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


if __name__ == '__main__':
    game = MainWindow(480, 480)
    game.show()

