import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Main App')
        width = 800
        height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.resizable(False, False)

        self.label = ttk.Label(self, text='Thinker Test', font=('Arial', 24, 'bold'), foreground='blue')
        self.label.pack()

        # write input and click me button
        self.input = ttk.Entry(self, font=('Arial', 16))
        self.input.pack()

        self.button = ttk.Button(self, text='Click Me', command=self.click_me)
        self.button.pack()

        self.label = ttk.Label(self, text='', font=('Arial', 16))
        self.label.pack()


    def click_me(self):
        #change button text
        self.button['text'] = 'Clicked'
        #change label text
        self.label['text'] = self.input.get()



    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.run()
