from tkinter import *


class Gui_choice2():
    x = None

    # rad2 = None
    # rad1 = None
    # rad3 = None
    # rad4 = None
    # rad5 = None

    def __init__(self):
        window = Tk()
        f = IntVar()
        f.set(0)
        self.window = window
        self.window.title("你想用自己的作文还是库里现成的作文？")
        self.window.geometry("700x250")
        rad1 = Radiobutton(self.window, text="自己写", var=f, value=1, width=10, command=self.clicked1)
        rad2 = Radiobutton(self.window, text="库第1篇", var=f, value=2, width=10, command=self.clicked2)
        rad3 = Radiobutton(self.window, text="库第2篇", var=f, value=3, width=10, command=self.clicked3)
        rad4 = Radiobutton(self.window, text="库第3篇", var=f, value=4, width=10, command=self.clicked4)
        rad5 = Radiobutton(self.window, text="库第4篇", var=f, value=5, width=10, command=self.clicked5)
        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        rad3.grid(column=3, row=0)
        rad4.grid(column=0, row=1)
        rad5.grid(column=1, row=1)
        # self.rad1 = rad1
        # self.rad3 = rad3
        # self.rad2 = rad2
        # self.rad4 = rad4
        # self.rad5 = rad5
        self.window.mainloop()

    def clicked1(self, ):
        self.x = 0
        self.window.destroy()

    def clicked2(self, ):
        self.x = 1
        self.window.destroy()

    def clicked3(self, ):
        self.x = 2
        self.window.destroy()

    def clicked4(self, ):
        self.x = 3
        self.window.destroy()

    def clicked5(self, ):
        self.x = 4
        self.window.destroy()

