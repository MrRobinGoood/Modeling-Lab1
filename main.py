import tkinter as tk


class KeyboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Modeling Lab1 Bartenev")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)

        self.label = tk.Label(self.master, text="Инфиксная строка", font=('Arial', 16))
        self.label.pack()

        self.entry = tk.Entry(self.master, font=('Arial', 20), state='readonly')
        self.entry.pack(pady=20)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack()

        self.alphabet = 'abcdefg'
        additional_chars = ['+', '-', '*', '/', 'sin(', 'cos(', 'arccos(', 'arcsin(', '(', ')']

        for letter in self.alphabet:
            button = tk.Button(self.buttons_frame, text=letter, font=('Arial', 16), width=3, height=1,
                               command=lambda l=letter: self.add_text(l))
            button.grid(row=0, column=self.alphabet.index(letter))

        for char in additional_chars:
            button = tk.Button(self.buttons_frame, text=char, font=('Arial', 16), width=5, height=1,
                               command=lambda c=char: self.add_text(c))
            button.grid(row=1, column=additional_chars.index(char))

        self.backspace_button = tk.Button(self.buttons_frame, text="<-", font=('Arial', 16), width=3, height=1,
                                          command=self.delete_last_char)
        self.backspace_button.grid(row=0, column=len(self.alphabet))

        self.clear_button = tk.Button(self.buttons_frame, text="Clear", font=('Arial', 16), width=6, height=1,
                                      command=self.clear_text)
        self.clear_button.grid(row=0, column=len(self.alphabet) + 1)

    def add_text(self, char):
        self.entry.config(state='normal')
        current_text = self.entry.get()
        if char.isalpha():
            if current_text != "" and current_text[-1].isalpha():
                self.entry.config(state='readonly')
                return
        if char in ['+', '-', '*', '/']:
            if current_text != "" and current_text[-1] in ['+', '-', '*', '/']:
                self.entry.config(state='readonly')
                return

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + char)
        self.entry.config(state='readonly')

    def delete_last_char(self):
        self.entry.config(state='normal')
        current_text = self.entry.get()
        if current_text.endswith("arcsin(") or current_text.endswith("arccos("):
            self.entry.delete(len(current_text) - 7, tk.END)
        elif current_text.endswith("sin(") or current_text.endswith("cos("):
            self.entry.delete(len(current_text) - 4, tk.END)
        else:
            self.entry.delete(len(current_text) - 1, tk.END)
        self.entry.config(state='readonly')

    def clear_text(self):
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.config(state='readonly')


def main():
    root = tk.Tk()




    app = KeyboardApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()


