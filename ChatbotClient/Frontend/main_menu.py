from tkinter import *
import ChatbotClient.Backend.client as cl
import threading
import time


class MainMenu:
    def __init__(self):
        self.root = Tk()

        #size of window
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        self.x = (self.ws / 2) - (700 / 2)
        self.y = (self.hs / 2) - (500 / 2)
        self.root.geometry('%dx%d+%d+%d' % (700, 500, self.x, self.y))
        self.root.resizable(False, False)
        self.root.minsize(300, 300)

        start_button = Button(self.root, text='Rozpocznij konwersację', highlightthickness=0, width=20, height=2, bg="#5856db",
                            fg="#ffffff", activebackground='#050430', activeforeground='#ffffff',
                            command=lambda : MainMenu.startChat(self))

        start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.mainloop()

    def startChat(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.deiconify()

        self.line = Label(self.root,
                          width=450,
                          bg="#000000")

        title_label = Label(self.root, text="CryptoChatbot", width=25, height=3, bg="#ffffff", fg="#5856db")
        title_label.config(font=("Courier", 24))
        title_label.place(relwidth=1, rely=0)

        self.conv_window = Text(self.root, width=20, height=2, bg="#5856db", fg="#ffffff", font="Helvetica 14",
                             padx=5, pady=5)

        self.conv_window.place(relheight=0.725, relwidth=0.95, relx=0.025, rely=0.2)

        self.bottom_label = Label(self.root, bg="#ffffff", height=75)

        self.bottom_label.place(relwidth=0.98, relx=0.01, rely=0.825)

        self.entry_msg = Entry(self.bottom_label, bg="#5856db", fg="#EAECEE", font="Helvetica 13")

        self.entry_msg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)

        self.entry_msg.focus()

        self.send_msg = Button(self.bottom_label, text="Send", font="Helvetica 10 bold", width=20, fg="#ffffff", bg="#5856db",
                               command= lambda: MainMenu.send_msg(self))


        self.send_msg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        self.send_msg.bind('<Return>', lambda event: MainMenu.send_msg(self))

        self.conv_window.config(cursor="arrow")

        scrollbar = Scrollbar(self.root, bg="#5856db")
        scrollbar.place(relheight=0.735, relwidth=0.95, relx=0.975, rely=0.15)
        scrollbar.config(command=self.conv_window.yview, takefocus=1)

        self.conv_window.config(state=DISABLED)




    def combine_funcs(*funcs, **kwargs):
        """
        :combine_funcs - Combine functions for command button
        """
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

    def send_msg(self):
        snd = threading.Thread(target=cl.send_message(self.entry_msg.get()))
        snd.start()
        self.conv_window.config(state=NORMAL)
        self.conv_window.insert(END,"Login: " + self.entry_msg.get() + "\n\n")

        self.conv_window.config(state=DISABLED)
        self.conv_window.see(END)
        self.entry_msg.delete(0, "end")

        rcv = threading.Thread(target=MainMenu.recive_msg(self))
        rcv.start()

    def recive_msg(self):
        while True:
            try:
                msg_length = cl.client.recv(cl.HEADER).decode(cl.FORMAT)
                if msg_length:
                    self.conv_window.config(state=NORMAL)
                    self.conv_window.insert(END, msg_length + "\n\n")
                    self.conv_window.see(END)
                    self.conv_window.config(state=DISABLED)
                    break
            except:
                print("error")




if __name__ == '__main__':
    new = MainMenu()