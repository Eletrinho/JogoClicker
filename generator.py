import time
import threading
import tkinter as tk

class Gerador():
    def __init__(self, name: str, cust: int, gen: int, total: tk.IntVar):
        self.name = name
        self.cust = cust
        self.gen = gen
        self.total = total
        self.quantity = tk.IntVar()

    def buy(self):
        if self.total.get() < self.cust:
            print('vc é pobre')
        else:
            self.quantity.set(self.quantity.get() + 1)
            self.total.set(self.total.get() - self.cust)

    def sell(self):
        if self.quantity > 0:
            self.quantity.set(self.quantity.get() - 1)

    def add(self):
        self.total.set(self.total.get() + self.gen * self.quantity.get())

    def gerando(self):
        while True:
            self.add()
            time.sleep(1)

    def iniciar_tarefa(self):
        thread_tarefa = threading.Thread(target=self.gerando)
        thread_tarefa.daemon = True
        thread_tarefa.start()