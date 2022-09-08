from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Login")
# root.geometry("300x250")
root.geometry("300x250+525+205")
Label(root, text="Please enter login details", font=("arial", 10, "bold")).pack()

name_inp = StringVar()
password_inp = StringVar()


def enter():
	if (name_inp.get() == "rohit" or "Rohit " or "rohit " or "vicky" or "vicky " or "sujeet") and (password_inp.get() == "king@12"):
		root.destroy()
		import main_2
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		name_inp.set("")
		password_inp.set("")


Label(root, text="").pack()
user_lbl = Label(root, text="Username").pack()
user_entry = Entry(root, textvariable=name_inp).pack()


Label(root, text="").pack()
pasword_lbl = Label(root, text="Password").pack()
paswrd_entry = Entry(root, textvariable=password_inp, show= '*')


paswrd_entry.pack()
Label(root, text="").pack()
Button(root, text="Login", command = enter, width=10, height=1).pack()
root.mainloop()



