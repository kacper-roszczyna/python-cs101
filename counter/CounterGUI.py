from counter.Counter import Counter
from counter.CounterPresenter import CounterPresenter
from counter.CounterView import CounterView
from tkinter import *
import tkinter as tk


class CounterApplication(tk.Frame, CounterView):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.presenter = CounterPresenter(Counter(0), self)
        self.create_widgets()

    def create_widgets(self):
        self.increment = tk.Button(self)
        self.create_button("+", self.presenter.increment, self.increment)
        self.decrement = tk.Button(self)
        self.create_button("-", self.presenter.decrement, self.decrement)
        self.quit = tk.Button(self)
        self.create_button("quit", self.master.destroy, self.quit)
        self.quit.pack(side="bottom")
        self.count_display = tk.Label(self)
        self.count_display["text"] = "0"
        self.count_display.pack(side="top")

    def create_button(self, label, action, button):
        button["text"] = label
        button["command"] = action
        button.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def show_count(self, count):
        self.count_display["text"] = str(count)

root = tk.Tk()
app = CounterApplication(master=root)
app.mainloop()