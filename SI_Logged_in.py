import tkinter as tk

class SI_Logged_in(tk.Frame):
	def __init__(self,master):
		mainpassenger_frame = tk.Frame(master.canvas, bg="white")
		mainpassenger_frame.place(relheight=1, relwidth=1)

		title_frame2 = tk.Frame(mainpassenger_frame, bg="#003145", bd=13)
		title_frame2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

		title_label2 = tk.Label(title_frame2, text="RAILWAY FINE SYSTEM", font=("Comic Sans MS", "62"), bg="#003145", fg="white", )
		title_label2.place(relheight=1, relwidth=1)

		personaldetails_button = tk.Button(mainpassenger_frame, text="Personal Details", font=("Helvetica", "17"), command=master.clickpersonaldetails)
		personaldetails_button.place(relx=0.1, rely=0.31)

		logout_button = tk.Button(mainpassenger_frame, text="Log out", font=("Helvetica", "17"))
		logout_button.place(relx=0.83, rely=0.31)

		si_label = tk.Label(mainpassenger_frame, text="Welcome, Station Incharge", bg="white", fg="black", font=("Comic Sans MS", "27"))
		si_label.place(relx=0.5, rely=0.26, relwidth=0.5, anchor="n")

		logout_button = tk.Button(mainpassenger_frame, text="Log out", font=("Helvetica", "17"), command=master.clicklogout)
		logout_button.place(relx=0.83, rely=0.31)