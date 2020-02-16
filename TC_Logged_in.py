import tkinter as tk

class TC_Logged_in(tk.Frame):
	def __init__(self,master):
		main_frame = tk.Frame(master.canvas, bg="white")
		main_frame.place(relheight=1, relwidth=1)

		title_frame = tk.Frame(main_frame, bg="#003145", bd=13)
		title_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

		title_label = tk.Label(title_frame, text="RAILWAY FINE SYSTEM", font=("Comic Sans MS", "62"), bg="#003145", fg="white", )
		title_label.place(relheight=1, relwidth=1)

		tc_label = tk.Label(main_frame, text="Welcome, Ticket Collector", bg="white", fg="black", font=("Comic Sans MS", "27"))
		tc_label.place(relx=0.5, rely=0.26, relwidth=0.5, anchor="n")

		addfine_button = tk.Button(main_frame, text="Add Fine", font=("Helvetica", "17"),command=master.clickaddfine)
		addfine_button.place(relx=0.1, rely=0.31)

		personaldetails_button = tk.Button(main_frame, text="Personal Details", font=("Helvetica", "17"), command=master.clickpersonaldetails)
		personaldetails_button.place(relx=0.195, rely=0.31)

		# allfines_button = tk.Button(main_frame, text="All Fines", font=("Helvetica", "17"))#, command=master.clickallfines)
		# allfines_button.place(relx=0.355, rely=0.31)

		logout_button = tk.Button(main_frame, text="Log out", font=("Helvetica", "17"), command=master.clicklogout)
		logout_button.place(relx=0.83, rely=0.31)

		self.details_frame = tk.Frame(main_frame, bg="white")
		self.details_frame.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.5)

		finedetails_title = tk.Label(self.details_frame, text="FINE DETAILS", bg="white", fg="black", font=("Copperplate", "15"))
		finedetails_title.place(relx=0.05, rely=0.05)

		username_label = tk.Label(self.details_frame, text="USERNAME", fg="black", bg="white", bd=0, font=("Arial", "13"))
		username_label.place(relx=0.35, rely=0.15)

		station_label = tk.Label(self.details_frame, text="STATION", fg="black", bg="white", bd=0, font=("Arial", "13"))
		station_label.place(relx=0.5, rely=0.15)

		amount_label = tk.Label(self.details_frame, text="AMOUNT", fg="black", bg="white", bd=0, font=("Arial", "13"))
		amount_label.place(relx=0.65, rely=0.15)

		# datetime_label = tk.Label(self.details_frame, text="DATE/TIME", fg="black", bg="white", bd=0, font=("Arial", "13"))
		# datetime_label.place(relx=0.7, rely=0.15)

		# tc_label = tk.Label(main_frame, text="Welcome, Ticket Collector", bg="white", fg="black", font=("Comic Sans MS", "27"))
		# tc_label.place(relx=0.30, rely=0.26, relwidth=0.5)





