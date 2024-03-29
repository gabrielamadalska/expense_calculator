import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        # ustawienia okienka GUI
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Expenses calculator")
        
        # napis na gorze strony
        self.label = tk.Label(self.root, text="Hello, I am your financial Assistance!", font=('Arial', 18))
        self.label.pack(padx=10, pady=10) # zmiany zostaja wrzucone do GUI
        
        self.textbox = tk.Text(self.root, heigh=1, font=('Arial', 10))
        self.textbox.pack(padx=5, pady=5)

        self.button = tk.Button(self.root, text = "Add your expense", font=('Arial', 10), command=self.show_message)
        self.button.pack(padx=5, pady=5)

        self.root.mainloop() # wyslwetla


    def show_message(self):
        text = self.textbox.get('1.0', tk.END).strip()  # Pobranie tekstu z pola tekstowego
        if text:  # Sprawdzenie, czy tekst nie jest pusty
            messagebox.showinfo(title="Expense", message=text)
        
moje_GUI = MyGUI()
