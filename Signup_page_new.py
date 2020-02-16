import tkinter as tk
import pymysql


class Signup_page(tk.Frame):
	def __init__(self,master):
		# global mainsignup_frame
		# global signup_frame
		# global signup_label
		# global name_label
		# global name_entry
		# global aadhar_label
		# global aadhar_entry
		# global username_label
		# global username_entry
		# global email_label
		# global email_entry
		# global age_label
		# global age_entry
		# global gender_label
		# global gender
		# global gender_option
		# global contact_label
		# global contact_entry
		# global finee_button
		# global ticketcollector_button
		# global stationincharge_button
		# global error_label

		self.var=tk.IntVar()

		mainsignup_frame = tk.Frame(master.canvas, bg="white")
		mainsignup_frame.place(relheight=1, relwidth=1)

		signup_frame = tk.Frame(master.canvas, bg="#003145", bd=13)
		signup_frame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.8, anchor="n")

		signup_label = tk.Frame(signup_frame, bg="white")
		signup_label.place(relheight=1, relwidth=1)

		# scrollbar = tk.Scrollbar(signup_label, orient="vertical")
		# signup_label.config(yscrollcommand=scrollbar.set)
		# scrollbar.config(command="signup_label.yview")
		# scrollbar.pack(side="right", fill="y")

		name_label = tk.Label(signup_label, text="Name", fg="black", font=("Helvetica", "17"))
		name_label.place(relx=0.15, rely=0.05)

		self.name_entry = tk.Entry(signup_label)
		self.name_entry.place(relx=0.4, rely=0.05)

		aadhar_label = tk.Label(signup_label, text="Aadhar No.", fg="black", font=("Helvetica", "17"))
		aadhar_label.place(relx=0.11, rely=0.125)

		self.aadhar_entry = tk.Entry(signup_label)
		self.aadhar_entry.place(relx=0.4, rely=0.125)

		email_label = tk.Label(signup_label, text="Email", fg="black", font=("Helvetica", "17"))
		email_label.place(relx=0.13, rely=0.2)

		self.email_entry = tk.Entry(signup_label)
		self.email_entry.place(relx=0.4, rely=0.2)

		username_label = tk.Label(signup_label, text="Username", fg="black", font=("Helvetica", "17"))
		username_label.place(relx=0.11, rely=0.275)

		self.username_entry = tk.Entry(signup_label)
		self.username_entry.place(relx=0.4, rely=0.275)

		password_label = tk.Label(signup_label, text="Password", fg="black", font=("Helvetica", "17"))
		password_label.place(relx=0.11, rely=0.35)

		self.password_entry = tk.Entry(signup_label, show="*")
		self.password_entry.place(relx=0.4, rely=0.35)

		confirmpassword_label = tk.Label(signup_label, text="Confirm Password", fg="black", font=("Helvetica", "17"))
		confirmpassword_label.place(relx=0.05, rely=0.425)

		self.confirmpassword_entry = tk.Entry(signup_label, show="*")
		self.confirmpassword_entry.place(relx=0.4, rely=0.425)

		gender_label = tk.Label(signup_label, text="Gender", fg="black", font=("Helvetica", "17"))
		gender_label.place(relx=0.13, rely=0.5)

		self.gender = tk.StringVar(signup_label)
		choices = ("Male", "Female", "Other")
		self.gender_option = tk.OptionMenu(signup_label, self.gender, *choices)
		self.gender_option.place(relx=0.5, rely=0.5, width=100)
		self.gender.set("Male")

		age_label = tk.Label(signup_label, text="Age", fg="black", font=("Helvetica", "17"))
		age_label.place(relx=0.16, rely=0.575)

		self.age_entry = tk.Entry(signup_label)
		self.age_entry.place(relx=0.4, rely=0.575)

		contact_label = tk.Label(signup_label, text="Contact No.", fg="black", font=("Helvetica", "17"))
		contact_label.place(relx=0.10, rely=0.65)

		self.contact_entry = tk.Entry(signup_label)
		self.contact_entry.place(relx=0.4, rely=0.65)

		self.passenger_button = tk.Radiobutton(signup_label, variable=self.var, value=1, text="Passenger")
		self.passenger_button.place(relx=0.15, rely=0.72)
		
		self.ticketcollector_button = tk.Radiobutton(signup_label, variable=self.var, value=2, text="Ticket Collector")
		self.ticketcollector_button.place(relx=0.15, rely=0.77)

		self.stationincharge_button = tk.Radiobutton(signup_label, variable=self.var, value=3, text="Station Incharge")
		self.stationincharge_button.place(relx=0.15, rely=0.82)

		self.register_button = tk.Button(signup_label, text="Register", font=("Helvetica", "14"), command=master.clickregisternew)
		self.register_button.place(relx=0.5, rely=0.90, relwidth=0.4, anchor="n")

		self.error_label = tk.Label(signup_label, text="", fg="red", font=("Times New Roman", "17"))
		self.error_label.place(relx=0.3, rely=0.85)


	