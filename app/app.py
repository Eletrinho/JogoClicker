import tkinter as tk
from generator import Gerador


def add(cps):
    global total
    total.set(total.get() + cps)

def main():
    cps = 1
    
    root = tk.Tk()
    global total
    total = tk.IntVar()
    root.geometry("400x300")
    root.resizable(True, True) 

    geradores = [
        Gerador('Gerador1', 10, 2, total),
        Gerador('Gerador2', 15, 3, total),
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
        tk.Button(frame, text=f'Vender {gerador.name}', command=gerador.sell).grid(column=3, row=row_counter + 1)
        gerador.iniciar_tarefa()  # Iniciar a tarefa de geração contínua
        row_counter += 2

    tk.Button(frame, text='+ 1 ', command=add).grid(column=0, row=row_counter + 1)

    root.mainloop()

if __name__ == "__main__":
    main()
