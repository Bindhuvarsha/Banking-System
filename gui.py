import tkinter as tk
from tkinter import ttk,messagebox,simpledialog
from bank import Bank

class BankGUI:
    def __init__(self,root):
        self.root=root
        self.bank=Bank()
        self.login()
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()
    def login(self):
        self.clear()
        self.root.title("Login")
        tk.Label(self.root,text="UserName").pack()
        u=tk.Entry(self.root)
        u.pack()
        tk.Label(self.root,text="Password").pack()
        p=tk.Entry(self.root,show="*")
        p.pack()
        
        def go():
            if u.get()=="admin" and p.get()=="admin123":
                self.menu()
            else:
                messagebox.showerror("Error","Invalid Credentials")
        tk.Button(self.root,text="Login",command=go).pack(pady=10)
        
    def menu(self):
        self.clear()
        for t,c in [("Create",self.create),
                    ("Deposit",self.deposit),
                    ("Withdraw",self.withdraw),
                    ("Transfer",self.Transfer),
                    ("Balance",self.balance),
                    ("View",self.view)]:
            tk.Button(self.root,text=t,width=20,command=c).pack(pady=3)

    def create(self):
        n=simpledialog.askstring("","Account No")
        name=simpledialog.askstring("","Name")
        b=simpledialog.askfloat("","Initial Balance")
        messagebox.showinfo("Result","created" if self.bank.create_account(n,name,b) else "Exist")
    
    def deposit(self):
        n=simpledialog.askstring("","Account No")
        a=simpledialog.askfloat("","Amount")
        messagebox.showinfo("Result","Success" if self.bank.deposit(n,a) else "Account Not Found")
    def withdraw(self):
        n=simpledialog.askstring("","Account No")
        a=simpledialog.askfloat("","Amount")
        messagebox.showinfo("Result","Success" if self.bank.withdraw(n,a) else "Account Not Found")
    def Transfer(self):
        f=simpledialog.askstring("","From Account No")
        t=simpledialog.askstring("","To Account No")
        a=simpledialog.askfloat("","amount to be Transferred")
        messagebox.showinfo("Result","Success"
        if self.bank.transfer(f,t,a) else "Transfer Failed")

    def balance(self):
        n=simpledialog.askstring("","Account No")
        messagebox.showinfo("Balance",str(self.bank.balance(n)))
    def view(self):
        w=tk.Toplevel(self.root)
        tv=ttk.Treeview(w,columns=("A","N","B"),show="headings")
        for c in ("A","N","B"):
            tv.heading(c,text=c)
        for acc in self.bank.accounts.values():
            tv.insert("",tk.END,values=acc.get_details())
            tv.pack(fill="both",expand=True)