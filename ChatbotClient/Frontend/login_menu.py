from tkinter import *
import main_menu

class LoginMenu:
    def __init__(self):
        self.root = Tk()

        #size of window
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        self.x = (self.ws / 2) - (330 / 2)
        self.y = (self.hs / 2) - (400 / 2)
        self.root.geometry('%dx%d+%d+%d' % (330, 400, self.x, self.y))
        self.root.resizable(False, False)

        self.login_frame = Frame(self.root, width=330, height=400, bg="#ffffff").place(relx=0, rely=0)
        LoginMenu.createLoginMenu(self)

    def createLoginMenu(self):
        LoginMenu.clear_window(self)
        self.root.title('Logowanie')

        title_label = Label(self.login_frame, text="CryptoChatbot", width=30, height=4, bg="#ffffff", fg="#5856db")

        label_login = Label(self.login_frame, text="Login: ", width=15, height=2, bg="#ffffff", fg="#5856db")
        entry_login = Entry(self.login_frame, width=20, borderwidth=0, highlightthickness=0, bg="#5856db", fg="#ffffff")

        label_password = Label(self.login_frame, text="Hasło: ", width=15, height=2, bg="#ffffff", fg="#5856db")
        entry_password = Entry(self.login_frame, width=20, borderwidth=0, highlightthickness=0, bg="#5856db", fg="#ffffff")
        entry_password.config(show="*")

        button_remember = Button(self.login_frame, text="Zapomniał*m hasła!", width=15, height=1, highlightthickness=0,
                                 bg="#ffffff", fg="#5856db",
                                 borderwidth=0, activebackground="#ffffff", activeforeground="#050430",
                                command = lambda: LoginMenu.rememberPassword(self))

        button_login = Button(self.login_frame, text="Zaloguj się", width=9, height=2, bg="#5856db", fg="#ffffff",
                              activebackground='#050430', activeforeground="#ffffff", highlightthickness=0,
                              command=lambda: main_menu.MainMenu.combine_funcs(self.root.destroy(), main_menu.MainMenu()))

        title_label.config(font=("Courier", 20))
        title_label.place(relx=-0.20, rely=-0.05)

        label_login.place(relx=0.05, rely=0.28)
        entry_login.place(relx=0.35, rely=0.3)

        label_password.place(relx=0.05, rely=0.38)
        entry_password.place(relx=0.35, rely=0.4)

        button_remember.place(relx=0.35, rely=0.47)

        button_login.place(relx=0.4, rely=0.75)

        self.root.mainloop()

    def rememberPassword(self):
        LoginMenu.clear_window(self)
        self.root.configure(background="#ffffff")
        self.root.title('Zapomniał*m hasła')
        title_label = Label(self.login_frame, text="CryptoChatbot", width=30, height=4, bg="#ffffff", fg="#5856db")

        label_info = Label(self.login_frame, text="Na podany adres e-mail zostanie wysłane nowe hasło.",
                           width=45, height=2, bg="#ffffff", fg="#5856db").place(relx=0.015, rely=0.2)
        label_email = Label(self.login_frame, text="Adres e-mail: ", width=10, height=2, bg="#ffffff", fg="#5856db").place(relx=0.09, rely=0.39)
        entry_email = Entry(self.login_frame, width=20, borderwidth=1, highlightthickness=0, bg="#5856db", fg="#ffffff")

        title_label.config(font=("Courier", 20))
        title_label.place(relx=-0.20, rely=-0.05)

        entry_email.place(relx=0.35, rely=0.41)

        send_button = Button(self.login_frame, text='Wyślij', highlightthickness=0, width=9, height=2, bg="#5856db",
                             fg="#ffffff", activebackground='#050430', activeforeground='#ffffff')

        send_button.place(relx=0.4, rely=0.7)
        cancel_button = Button(self.login_frame, bg="#5856db", text='Anuluj', highlightthickness=0, width=6, height=1,
                               fg='#ffffff', activebackground='#050430', activeforeground='#ffffff', command= lambda: LoginMenu.createLoginMenu(self))

        cancel_button.place(relx=0.433, rely=0.85)


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    new = LoginMenu()