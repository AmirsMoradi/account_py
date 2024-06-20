import tkinter as tk
from tkinter import messagebox


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        if username == "admin" and password == "password":
            self.destroy()
            app = BankingApp()
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


class BankingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banking App")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Transfer money button
        self.transfer_button = tk.Button(self, text="Transfer Money", command=self.transfer_money)
        self.transfer_button.pack(pady=10)

        self.add_customer_button = tk.Button(self, text="Add Customer", command=self.add_customer)
        self.add_customer_button.pack(pady=10)

        # Remove customer button
        self.remove_customer_button = tk.Button(self, text="Remove Customer", command=self.remove_customer)
        self.remove_customer_button.pack(pady=10)

        self.admin_button = tk.Button(self, text="Admin Access", command=self.admin_access)
        self.admin_button.pack(pady=10)

    def transfer_money(self):
        messagebox.showinfo("Transfer Money", "Transfer Money functionality")

    def add_customer(self):
        messagebox.showinfo("Add Customer", "Add Customer functionality")

    def remove_customer(self):
        messagebox.showinfo("Remove Customer", "Remove Customer functionality")

    def admin_access(self):
        admin_window = AdminWindow(self)
        admin_window.grab_set()


class AdminWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Admin Panel")
        self.geometry("300x200")

        tk.Label(self, text="Admin Panel", font=("Arial", 14)).pack(pady=10)

        # Additional admin functionalities
        self.manage_accounts_button = tk.Button(self, text="Manage Accounts", command=self.manage_accounts)
        self.manage_accounts_button.pack(pady=5)

        self.view_reports_button = tk.Button(self, text="View Reports", command=self.view_reports)
        self.view_reports_button.pack(pady=5)

    def manage_accounts(self):
        messagebox.showinfo("Manage Accounts", "Manage Accounts functionality")

    def view_reports(self):
        messagebox.showinfo("View Reports", "View Reports functionality")


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()