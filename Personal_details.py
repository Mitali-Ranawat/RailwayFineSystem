import tkinter as tk
# import Root
# import Login_page
# import Signup_page

class Personal_details(tk.Frame):
	def __init__(self,master):

		mainpassenger_frame = tk.Frame(master.canvas, bg="white")
		mainpassenger_frame.place(relheight=1, relwidth=1)

		title_frame2 = tk.Frame(mainpassenger_frame, bg="#003145", bd=13)
		title_frame2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

		title_label2 = tk.Label(title_frame2, text="RAILWAY FINE SYSTEM", font=("Comic Sans MS", "62"), bg="#003145", fg="white", )
		title_label2.place(relheight=1, relwidth=1)

		back_button = tk.Button(mainpassenger_frame, text="< Back", font=("Helvetica", "17"))
		back_button.place(relx=0.1, rely=0.31)

		logout_button = tk.Button(mainpassenger_frame, text="Log out", font=("Helvetica", "17"), command=master.clicklogout)
		logout_button.place(relx=0.83, rely=0.31)

		details_frame = tk.Frame(mainpassenger_frame, bg="#003145", bd=13)
		details_frame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.60)

		details_label = tk.Frame(details_frame, bg="white")
		details_label.place(relheight=1, relwidth=1)

		personaldetails_label = tk.Label(details_label, text="PERSONAL DETAILS", fg="black", font=("Copperplate", "24"))
		personaldetails_label.place(relx=0.05, rely=0.05)

		self.mycursor = master.database()

		self.mycursor.execute('SELECT finee_username FROM finee')
		self.finee_list = self.mycursor.fetchall()
		self.finee_list = list(sum(self.finee_list, ()))
		self.mycursor.execute('SELECT finer_username FROM finer')
		self.finer_list = self.mycursor.fetchall()
		self.finer_list = list(sum(self.finer_list, ()))

		if master.user in self.finee_list:
			back_button.configure(command=master.clickbackpassenger)

			self.username_query = 'SELECT finee_username FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.username_query % master.user)
			username = self.mycursor.fetchall()
			username_label = tk.Label(details_label, text="Username: ", fg="black", font=("Helvetica", "20"))
			username_label1 = tk.Label(details_label, text="".join(x[0] for x in username), fg="black", font=("Helvetica", "20"))
			username_label.place(relx=0.1, rely=0.20)
			username_label1.place(relx=0.4, rely=0.20)

			self.name_query = 'SELECT finee_name FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.name_query %master.user)
			name = self.mycursor.fetchall()
			name_label = tk.Label(details_label, text="Name: ", fg="black", font=("Helvetica", "20"))
			name_label.place(relx=0.1, rely=0.30)
			name_label1 = tk.Label(details_label, text="".join(x[0] for x in name), fg="black", font=("Helvetica", "20"))
			name_label1.place(relx=0.4, rely=0.30)

			self.email_query = 'SELECT email FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.email_query %master.user)
			email = self.mycursor.fetchall() 
			email_label = tk.Label(details_label, text="Email ID: ", fg="black", font=("Helvetica", "20"))
			email_label.place(relx=0.1, rely=0.40)
			email_label1 = tk.Label(details_label, text="".join(x[0] for x in email), fg="black", font=("Helvetica", "20"))
			email_label1.place(relx=0.4, rely=0.40)

			self.aadhar_query = 'SELECT aadhar_card FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.aadhar_query %master.user)
			aadhar = self.mycursor.fetchall() 
			aadhar_label = tk.Label(details_label, text="Aadhar ID: ", fg="black", font=("Helvetica", "20"))
			aadhar_label.place(relx=0.1, rely=0.50)
			aadhar_label1 = tk.Label(details_label, text="".join(x[0] for x in aadhar), fg="black", font=("Helvetica", "20"))
			aadhar_label1.place(relx=0.4, rely=0.50)

			self.gender_query = 'SELECT gender FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.gender_query %master.user)
			gender = self.mycursor.fetchall() 
			gender_label = tk.Label(details_label, text="Gender: ", fg="black", font=("Helvetica", "20"))
			gender_label.place(relx=0.1, rely=0.60)
			gender_label1 = tk.Label(details_label, text="".join(x[0] for x in gender), fg="black", font=("Helvetica", "20"))
			gender_label1.place(relx=0.4, rely=0.60)

			self.age_query = 'SELECT age FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.age_query %master.user)
			age = self.mycursor.fetchall() 
			age_label = tk.Label(details_label, text="Age: ", fg="black", font=("Helvetica", "20"))
			age_label.place(relx=0.1, rely=0.70)
			age_label1 = tk.Label(details_label, text="".join(x[0] for x in age), fg="black", font=("Helvetica", "20"))
			age_label1.place(relx=0.4, rely=0.70)

			self.contact_query = 'SELECT contact_no FROM finee WHERE finee_username="%s" '
			self.mycursor.execute(self.contact_query %master.user)
			contact = self.mycursor.fetchall() 
			contact_label = tk.Label(details_label, text="Contact No.: ", fg="black", font=("Helvetica", "20"))
			contact_label.place(relx=0.1, rely=0.80)
			contact_label1 = tk.Label(details_label, text="".join(x[0] for x in contact), fg="black", font=("Helvetica", "20"))
			contact_label1.place(relx=0.4, rely=0.80)

		elif master.user in self.finer_list:
			back_button.configure(command=master.clickbacktc)
			self.username_query = 'SELECT finer_username FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.username_query % master.user)
			username = self.mycursor.fetchall()
			username_label = tk.Label(details_label, text="Username: ", fg="black", font=("Helvetica", "20"))
			username_label1 = tk.Label(details_label, text="".join(x[0] for x in username), fg="black", font=("Helvetica", "20"))
			username_label.place(relx=0.1, rely=0.20)
			username_label1.place(relx=0.4, rely=0.20)

			self.name_query = 'SELECT finer_name FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.name_query %master.user)
			name = self.mycursor.fetchall()
			name_label = tk.Label(details_label, text="Name: ", fg="black", font=("Helvetica", "20"))
			name_label.place(relx=0.1, rely=0.30)
			name_label1 = tk.Label(details_label, text="".join(x[0] for x in name), fg="black", font=("Helvetica", "20"))
			name_label1.place(relx=0.4, rely=0.30)

			self.email_query = 'SELECT email FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.email_query %master.user)
			email = self.mycursor.fetchall() 
			email_label = tk.Label(details_label, text="Email ID: ", fg="black", font=("Helvetica", "20"))
			email_label.place(relx=0.1, rely=0.40)
			email_label1 = tk.Label(details_label, text="".join(x[0] for x in email), fg="black", font=("Helvetica", "20"))
			email_label1.place(relx=0.4, rely=0.40)

			self.aadhar_query = 'SELECT aadhar_card FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.aadhar_query %master.user)
			aadhar = self.mycursor.fetchall() 
			aadhar_label = tk.Label(details_label, text="Aadhar ID: ", fg="black", font=("Helvetica", "20"))
			aadhar_label.place(relx=0.1, rely=0.50)
			aadhar_label1 = tk.Label(details_label, text="".join(x[0] for x in aadhar), fg="black", font=("Helvetica", "20"))
			aadhar_label1.place(relx=0.4, rely=0.50)

			self.gender_query = 'SELECT gender FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.gender_query %master.user)
			gender = self.mycursor.fetchall() 
			gender_label = tk.Label(details_label, text="Gender: ", fg="black", font=("Helvetica", "20"))
			gender_label.place(relx=0.1, rely=0.60)
			gender_label1 = tk.Label(details_label, text="".join(x[0] for x in gender), fg="black", font=("Helvetica", "20"))
			gender_label1.place(relx=0.4, rely=0.60)

			self.age_query = 'SELECT age FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.age_query %master.user)
			age = self.mycursor.fetchall() 
			age_label = tk.Label(details_label, text="Age: ", fg="black", font=("Helvetica", "20"))
			age_label.place(relx=0.1, rely=0.70)
			age_label1 = tk.Label(details_label, text="".join(x[0] for x in age), fg="black", font=("Helvetica", "20"))
			age_label1.place(relx=0.4, rely=0.70)

			self.contact_query = 'SELECT contact_no FROM finer WHERE finer_username="%s" '
			self.mycursor.execute(self.contact_query %master.user)
			contact = self.mycursor.fetchall() 
			contact_label = tk.Label(details_label, text="Contact No.: ", fg="black", font=("Helvetica", "20"))
			contact_label.place(relx=0.1, rely=0.80)
			contact_label1 = tk.Label(details_label, text="".join(x[0] for x in contact), fg="black", font=("Helvetica", "20"))
			contact_label1.place(relx=0.4, rely=0.80)

			# self.post_query = 'SELECT finer_name FROM finer WHERE finer_username="%s" '
			# self.mycursor.execute(self.post_query %master.user)
			# post = self.mycursor.fetchall()
			# post_label = tk.Label(details_label, text="Post: ", fg="black", font=("Helvetica", "20"))
			# post_label.place(relx=0.1, rely=0.90)
			# post_label1 = tk.Label(details_label, text="".join(x[0] for x in post), fg="black", font=("Helvetica", "20"))
			# post_label1.place(relx=0.4, rely=0.90)


		
