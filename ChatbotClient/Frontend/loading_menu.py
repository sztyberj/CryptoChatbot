from tkinter import *
from tkinter import font
import ChatbotClient.Frontend.main_menu
import time


class LoadingWindow:
    def __init__(self):
        self.root = Tk()

        # True - hide main bar window
        self.root.overrideredirect(1)

        # size of window
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        self.x = (self.ws / 2) - (400 / 2)
        self.y = (self.hs / 2) - (250 / 2)
        self.root.geometry('%dx%d+%d+%d' % (400, 250, self.x, self.y))
        self.root.resizable(False, False)

        self.root.resizable(False, False)
        self.root.configure(background='#ffffff')

        self.canvas_width = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=30, background='#ffffff', bd=0, highlightthickness=0, relief='ridge')

        self.Tittle = 'CryptoChatbot'
        self.TittleFont = font.Font(family="Helvetica", size=25, weight="bold")
        self.FootFont = font.Font(size=10)

        self.MainBar = Label(self.root, width=16, background="#ffffff", text=self.Tittle, font=self.TittleFont, foreground='#5856db')
        self.FootBar = Label(self.root, background="#ffffff", text="Created by Jakub Sztyber", foreground='black', font=self.FootFont)


        self.rectangle = self.canvas.create_rectangle(50, 50,  0, 0, outline='#5856db',fill='#5856db')


        self.canvas.place(relx=0, rely=0.6)
        self.MainBar.place(relx=0.13, rely=0.25)
        self.FootBar.place(relx=0.55, rely=0.85)

        LoadingWindow.LoadingAnimation(self)
        self.root.mainloop()
        self.main_menu = ChatbotClient.Frontend.main_menu.MainMenu()


    def LoadingAnimation(self):

        for x in range(70):
            xspeed = 5
            yspeed = 0
            self.canvas.move(self.rectangle, xspeed, yspeed)
            time.sleep(0.03)
            self.root.update()
        for y in range(70):
            xspeed = -5
            yspeed = 0
            self.canvas.move(self.rectangle, xspeed, yspeed)
            time.sleep(0.03)
            self.root.update()
        self.root.destroy()

if __name__ == '__main__':
    OpenWindow = LoadingWindow()