import tkinter as tk
from tkinter import messagebox

class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Atividade 26-04")
        self.root.geometry("400x500")

        #Interface
        tk.Label(root, text="Número de discos:", font=("Arial", 10)).pack(pady=5)
        
        self.entry_discos = tk.Entry(root, justify='center')
        self.entry_discos.pack(pady=5)
        self.entry_discos.insert(0, "3")

        self.btn_resolver = tk.Button(root, text="Resolver", command=self.iniciar_hanoi)
        self.btn_resolver.pack(pady=10)

        #Movimentos
        tk.Label(root, text="Movimentos:", font=("Arial", 10,)).pack()
        
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.frame_lista, yscrollcommand=self.scrollbar.set, font=("Courier", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        self.label_total = tk.Label(root, text="Total de movimentos: 0", font=("Arial", 10, "italic"))
        self.label_total.pack(pady=10)

    def iniciar_hanoi(self):

        self.listbox.delete(0, tk.END)
        
        try:
            n = int(self.entry_discos.get())
            if n < 1:
                messagebox.showwarning("Aviso", "Insira um número maior que zero.")
                return
            if n > 15:
                if not messagebox.askyesno("Aviso", "Muitos discos podem travar a interface. Continuar?"):
                    return

            movimentos = []
            self.resolver_recursivo(n, 'Haste A', 'Haste C', 'Haste B', movimentos)
            

            for i, mov in enumerate(movimentos, 1):
                self.listbox.insert(tk.END, f"[{i:02d}] {mov}")
            
            self.label_total.config(text=f"Total de movimentos: {len(movimentos)}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número inteiro válido.")

    def resolver_recursivo(self, n, origem, destino, auxiliar, lista):
        if n == 1:
            lista.append(f"Disco 1: {origem} ➔ {destino}")
            return

        self.resolver_recursivo(n - 1, origem, auxiliar, destino, lista)
        lista.append(f"Disco {n}: {origem} ➔ {destino}")
        self.resolver_recursivo(n - 1, auxiliar, destino, origem, lista)


if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGUI(root)
    root.mainloop()
