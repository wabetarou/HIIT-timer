import time
import tkinter as tk

class HIITClock():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("今日も頑張ろう！！！")
        self.root.geometry("800x500+300+100")
        self.timer = Timer(self.root)
        self.flag = tk.Label(text="", font=('Helvetica', 48), fg='white')
        self.action = tk.Label(text="", font=('Helvetica', 48), fg='white')
        self.label = tk.Label(text="", font=('Helvetica', 480), fg='white')
        self.flag.pack()
        self.action.pack()
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.label.configure(text=self.timer.time)
        self.flag.configure(text=self.timer.flag)
        self.action.configure(text=self.timer.action)
        self.timer.call()
        self.root.after(1000, self.update_clock)

class Timer():
    def __init__(self, root):
        self.time = 185
        self.flag = 0
        self.end = 0
        self.action = "ウォーミングアップ"
        self.root = root

    def call(self):
        self.time -= 1
        if self.time < 0:
            if self.flag == 8:
                self.flag += 2
                self.time = 60
                self.action = "一分間休憩。。。"
            elif self.flag == 18:
                self.root.destroy()
            elif self.flag % 2 == 0:
                self.flag += 1
                self.time = 20
                self.action = "本気でやる！！！"
            elif self.flag % 2 == 1:
                self.flag +=1
                self.time = 10
                self.action = "休憩。。。"






app = HIITClock()