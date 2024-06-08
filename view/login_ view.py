from tkinter import *
import tkinter.messagebox as msg

from model.tools.logging import Logger
from view.person_view import PersonView
from view.commpotent.lable_text import TextWithLabel


class LoginView:
    def login_click(self):
        status, person = PersonController.find_by_username_and_password(self.username.variable.get(), self.password.variable.get())
        if status:
            Logger.info(f"Login Successful ({self.username.variable.get()} : {self.password.variable.get()})")
            self.win.destroy()
            ui = PersonView(person)
        else:
            Logger.error(f"Login Error ({self.username.variable.get()} : {self.password.variable.get()})")
            msg.showerror("Login", "Wrong Username/Password !!!")

    def __init__(self):
        Logger.info("App Started")
        self.win = Tk()
        self.win.geometry("250x200")
        self.win.title("Login")

        self.username = TextWithLabel(self.win, "Username", 20, 40)
        self.password = TextWithLabel(self.win, "Password", 20, 80)

        Button(self.win, text="Login", width=10, command=self.login_click).place(x=80, y=150)

        self.win.mainloop()


