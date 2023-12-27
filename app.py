import tkinter as tk
import time
import threading

class Gerador():
    def __init__(self, name: str, cust: int, gen: int):
        self.name = name
        self.cust = cust
        self.gen = gen
        self.quantity = tk.IntVar()

    def buy(self):
        global total
        if total.get() < self.cust:
            print('vc é pobre')
        else:
            self.quantity.set(self.quantity.get() + 1)
            total.set(total.get() - self.cust)

    def sell(self):
        self.quantity.set(self.quantity.get() - 1)

    def add(self):
        global total
        total.set(total.get() + self.gen * self.quantity.get())

    def gerando(self):
        while True:
            self.add()
            time.sleep(1)

    def iniciar_tarefa(self):
        thread_tarefa = threading.Thread(target=self.gerando)
        thread_tarefa.daemon = True
        thread_tarefa.start()

def add():
    global total
    total.set(total.get() + 1)

def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(True, True) 

    global total
    total = tk.IntVar()

    geradores = [
        Gerador('Gerador1', 1, 2),
        Gerador('Gerador2', 2, 3),
        # Adicione mais geradores conforme necessário
    ]

    frame = tk.Frame(root, padx=10, pady=10)
    frame.grid()

    tk.Label(frame, text='Total').grid(column=0, row=0)
    tk.Label(frame, textvariable=total).grid(column=1, row=0)
    
    row_counter = 1
    for gerador in geradores:
        tk.Label(frame, text=f"Quantidade gerada por {gerador.name}: {gerador.gen}").grid(column=2, row=row_counter)
        tk.Button(frame, text=f'Compra {gerador.name}', command=gerador.buy).grid(column=2, row=row_counter + 1)
        tk.Button(frame, text=f'Vender {gerador.name}', command=gerador.sell).grid(column=2, row=row_counter + 2)
        gerador.iniciar_tarefa()  # Iniciar a tarefa de geração contínua
        row_counter += 3
    tk.Button(frame, text='+ 1 ', command=add).grid(column=0, row=row_counter + 1)

    root.mainloop()

if __name__ == "__main__":
    main()
