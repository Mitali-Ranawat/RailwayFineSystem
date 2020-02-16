import tkinter as tk

class Login_page(tk.Frame):
	def __init__(self,master):
		# global mainlogin_frame
		# global title_frame
		# global title_label
		# global login_frame
		# global login_label
		# global username_label
		# global username_entry
		# global password_label
		# global password_entry
		# global login_button
		# global signup_label
		# global signup_button

		mainlogin_frame = tk.Frame(master.canvas, bg="white")
		mainlogin_frame.place(relheight=1, relwidth=1)

		title_frame = tk.Frame(mainlogin_frame, bg="#003145", bd=13)
		title_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.2)

		title_label = tk.Label(title_frame, text="RAILWAY FINE SYSTEM", font=("Comic Sans MS", "62"), bg="#003145", fg="white", )
		title_label.place(relheight=1, relwidth=1)

		login_frame = tk.Frame(mainlogin_frame, bg="#003145", bd=13)
		login_frame.place(relx=0.5, rely=0.45, relwidth=0.4, relheight=0.45, anchor="n")

		login_label = tk.Frame(login_frame, bg="white")
		login_label.place(relheight=1, relwidth=1)

		username_label = tk.Label(login_label, text="Username", fg="black", font=("Helvetica", "17"))
		username_label.place(relx=0.1, rely=0.25)

		self.username_entry = tk.Entry(login_label)
		self.username_entry.place(relx=0.4, rely=0.25)

		password_label = tk.Label(login_label, text="Password", fg="black", font=("Helvetica", "17"))
		password_label.place(relx=0.1, rely=0.4)

		self.password_entry = tk.Entry(login_label, show="*")
		self.password_entry.place(relx=0.4, rely=0.4)

		login_button = tk.Button(login_label, text="Login", font=("Helvetica", "14"), command=master.clicklogin)
		login_button.place(relx=0.5, relwidth=0.5, anchor="n", rely=0.60)

		signup_label = tk.Label(login_label, text="Not registered yet? ", font=("Helvetica", "14"))
		signup_label.place(relx=0.5, rely=0.73, relwidth=0.5, anchor="n")

		signup_button = tk.Button(login_label, text="Signup", command=master.clicksignup)
		signup_button.place(relx=0.5, rely=0.80, relwidth=0.2, anchor="n")

		self.error_login = tk.Label(login_label, text="", fg="red", font=("Times New Roman", "17"))
		self.error_login.place(relx=0.5, rely=0.55, relwidth=0.5, anchor="n")
