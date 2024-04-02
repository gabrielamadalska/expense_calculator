import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        # ustawienia okienka GUI
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        
        # pasek zadan
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing) 
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit without asking", command=exit)

        self.menubar.add_cascade(menu=self.filemenu, label = "File")

        self.root.config(menu=self.menubar)

        # rozmiar okienka GUI
        self.root.geometry("250x150")
        self.root.title("Expenses calculator")
        
        # frame = tk.Frame(self.root)
        # frame.grid(row=0, column=0)  # lub frame.pack(...)
        # self.textbox = tk.Text(frame, height=1, font=('Arial', 10))
        # self.textbox.pack(padx=50, pady=5, anchor='e')


        self.income_label = tk.Label(self.root, text="Income:")
        self.income_label.grid(row=0, column=0, padx=10, pady=5)
        self.income_entry = tk.Entry(self.root)
        self.income_entry.grid(row=0, column=1, padx=10, pady=5)

        self.outcome_label = tk.Label(self.root, text="Outcome:")
        self.outcome_label.grid(row=1, column=0, padx=10, pady=5)
        self.outcome_entry = tk.Entry(self.root)
        self.outcome_entry.grid(row=1, column=1, padx=10, pady=5)


        # przycisk
        self.button = tk.Button(self.root, text = "Calculate", font=('Arial', 10), command=self.calculate)
        self.button.grid(row=2, column=1, padx=10, pady=5, )

        self.saving_label = tk.Label(self.root, text="Savings: ")
        self.saving_label.grid(row=3, column=1, padx=10, pady=5)

        self.root.mainloop() # wyslwetla

    def show_message(self):
        text = self.textbox.get('1.0', tk.END).strip()  # Pobranie tekstu z pola tekstowego
        if text:  # Sprawdzenie, czy tekst nie jest pusty
            messagebox.showinfo(title="Expense", message=text)

    def on_closing(self):
        if messagebox.askyesno(title="Quit", message="You wanna quit?"):
            self.root.destroy()
        
    def calculate(self):
        try:
            income = float(self.income_entry.get())
            outcome = float(self.outcome_entry.get())
            savings = income - outcome
            self.saving_label.config(text="Savings: {:.2f}".format(savings))
        except ValueError as e:
            self.saving_label.config(text="Value error")

moje_GUI = MyGUI()
