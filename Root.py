import tkinter as tk
import pymysql
import Login_page
import Signup_page
#import Signup_page_Incharge
import Passenger_Logged_in
import TC_Logged_in
import SI_Logged_in
import Add_fine
import Personal_details

class Root(tk.Frame):  
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.master.title("Railway Fine System")
		self.master.resizable(False,False)
		self.master.geometry("1200x800")
		self.master.protocol("WM_DELETE_WINDOW", self.clickcancel)
		self.master.bind("<Escape>", self.clickescape)
		self.pack()
		self.canvas = tk.Canvas(root).pack()
		# self.addfine = Add_fine.Add_fine(self)
		# self.passenger_loggedin = Passenger_Logged_in.Passenger_Logged_in(self)
		# self.tc_loggedin = TC_Logged_in.TC_Logged_in(self)
		# self.si_loggedin = SI_Logged_in.SI_Logged_in(self)
		# self.signuppage = Signup_page_P.Signup_page(self)
		# self.insignuppage = Signup_page_Incharge.Signup_page(self)
		# self.personal_details = Personal_details.Personal_details(self)
		self.loginpage = Login_page.Login_page(self)

	def database(self):
		self.mydb=pymysql.connect(host='localhost',user='root',passwd='',db='railway_fine_system')
		self.mycursor=self.mydb.cursor()
		return self.mycursor

	def clickcancel(self):
		self.master.destroy()

	def clickescape(self,event):
		self.master.destroy()
	
	def clicksignup(self):
		self.signuppage = Signup_page.Signup_page(self)
	
	def clickregister(self):
		self.signuppage.error_label.configure(text="")

		name = self.signuppage.name_entry.get()
		aadhar = self.signuppage.aadhar_entry.get()
		email = self.signuppage.email_entry.get()
		username = self.signuppage.username_entry.get()
		password = self.signuppage.password_entry.get()
		confirm = self.signuppage.confirmpassword_entry.get()
		gender = self.signuppage.gender.get()
		age = self.signuppage.age_entry.get()
		contact = self.signuppage.contact_entry.get()

		flag=1
		if name=="" or aadhar=="" or email=="" or username=="" or password=="" or confirm=="" or gender=="" or age=="" or contact=="":
			self.signuppage.error_label.configure(text="One or more fields are empty!!")
			flag=0
		elif not name.isalnum() or not aadhar.isdigit() or not age.isdigit() or not contact.isdigit():
			self.signuppage.error_label.configure(text="Invalid data entry!!")
			flag=0
		elif len(aadhar)!=12:
			self.signuppage.error_label.configure(text="Invalid adhar number!!")
			flag=0
		elif len(username)>15:
			self.signuppage.error_label.configure(text="Username cannot have more than 15 characters!!")
			flag=0
		elif len(contact)!=10:
			self.signuppage.error_label.configure(text="Invalid contact number!!")
			flag=0
		elif self.signuppage.var.get() not in (1,2,3):
			self.signuppage.error_label.configure(text="User type not specified!!")
			flag=0

		if flag==1:
			self.signuppage.error_label.configure(text="")
			if(confirm!=password):
				self.signuppage.error_label.configure(text="Password doesn't match!!")
			else:
				self.mycursor = self.database()
				self.button_value = self.signuppage.var.get()
				if self.button_value==1:
					self.mycursor.execute('INSERT INTO finee(finee_name, finee_username, finee_password, email, aadhar_card, gender, age, contact_no) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()
				elif self.button_value==2:
					self.mycursor.execute('INSERT INTO finer(finer_name, finer_username, finer_password, email, aadhar_card, gender, age, contact_no, post) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Ticket Collector")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()
				elif self.button_value==3:
					self.mycursor.execute('INSERT INTO finer(finer_name, finer_username, finer_password, email, aadhar_card, gender, age, contact_no, post) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Station Incharge")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()
				
				self.loginpage = Login_page.Login_page(self)

	def clickregisternew(self):
		self.signuppage.error_label.configure(text="")

		name = self.signuppage.name_entry.get()
		aadhar = self.signuppage.aadhar_entry.get()
		email = self.signuppage.email_entry.get()
		username = self.signuppage.username_entry.get()
		password = self.signuppage.password_entry.get()
		confirm = self.signuppage.confirmpassword_entry.get()
		gender = self.signuppage.gender.get()
		age = self.signuppage.age_entry.get()
		contact = self.signuppage.contact_entry.get()

		flag=1
		if name=="" or aadhar=="" or email=="" or username=="" or password=="" or confirm=="" or gender=="" or age=="" or contact=="":
			self.signuppage.error_label.configure(text="One or more fields are empty!!")
			flag=0
		elif not name.isalnum() or not aadhar.isdigit() or not age.isdigit() or not contact.isdigit():
			self.signuppage.error_label.configure(text="Invalid data entry!!")
			flag=0
		elif len(aadhar)!=12:
			self.signuppage.error_label.configure(text="Invalid adhar number!!")
			flag=0
		elif len(username)>15:
			self.signuppage.error_label.configure(text="Username cannot have more than 15 characters!!")
			flag=0
		elif len(contact)!=10:
			self.signuppage.error_label.configure(text="Invalid contact number!!")
			flag=0
		elif self.signuppage.var.get() not in (1,2,3):
			self.signuppage.error_label.configure(text="User type not specified!!")
			flag=0

		if flag==1:
			self.signuppage.error_label.configure(text="")
			if(confirm!=password):
				self.signuppage.error_label.configure(text="Password doesn't match!!")
			else:
				self.mycursor = self.database()
				self.button_value = self.signuppage.var.get()
				if self.button_value==1:
					self.mycursor.execute('INSERT INTO finee(finee_name, finee_username, finee_password, email, aadhar_card, gender, age, contact_no) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()
				elif self.button_value==2:
					self.mycursor.execute('INSERT INTO finer(finer_name, finer_username, finer_password, email, aadhar_card, gender, age, contact_no, post) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Ticket Collector")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()
				elif self.button_value==3:
					self.mycursor.execute('INSERT INTO finer(finer_name, finer_username, finer_password, email, aadhar_card, gender, age, contact_no, post) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "Station Incharge")'%(name, username, password, email, aadhar, gender, age, contact))
					self.mydb.commit()

				self.addfine = Add_fine.Add_fine(self)



	def clicklogin(self):
		self.loginpage.error_login.configure(text="")
		username = self.loginpage.username_entry.get()
		password = self.loginpage.password_entry.get()
		if username=="" or password=="":
			self.loginpage.error_login.configure(text="Username or Password not entered!!")
		else:
			self.loginpage.error_login.configure(text="")
			self.mycursor = self.database()
			self.mycursor.execute('SELECT finee_username FROM finee')
			self.finee_list = self.mycursor.fetchall()
			self.finee_list = list(sum(self.finee_list, ()))
			self.mycursor.execute('SELECT finer_username FROM finer')
			self.finer_list = self.mycursor.fetchall()
			self.finer_list = list(sum(self.finer_list, ()))
			self.final_list = self.finee_list+self.finer_list
			if username not in self.final_list: #or self.finer_list:
				self.loginpage.error_login.configure(text="Invalid username!!")
			else:
				if username in self.finee_list:	
					self.query1 = 'SELECT finee_password FROM finee WHERE finee_username="%s" '
					self.mycursor.execute(self.query1 % username)
					self.finee_password = self.mycursor.fetchall()
					self.finee_password = list(sum(self.finee_password, ()))
					if password not in self.finee_password:
						self.loginpage.error_login.configure(text="Invalid password!!")
					else:
						self.user = username
						self.passenger_loggedin = Passenger_Logged_in.Passenger_Logged_in(self)
						self.passengerfines()-
				elif username in self.finer_list:
					self.query1 = 'SELECT finer_password FROM finer WHERE finer_username="%s" '
					self.mycursor.execute(self.query1 % username)
					self.finer_password = self.mycursor.fetchall()
					self.finer_password = list(sum(self.finer_password, ()))
					if password not in self.finer_password:
						self.loginpage.error_login.configure(text="Invalid password!!")
					else:
						self.user = username
						self.mycursor.execute('SELECT post FROM finer WHERE finer_username="%s" ' %(username))
						self.post = self.mycursor.fetchall()
						self.post = list(sum(self.post, ()))
						self.tc_loggedin = TC_Logged_in.TC_Logged_in(self)
						self.finedetails()
						# elif self.post[0]=="Station Incharge":
						# 	self.si_loggedin = SI_Logged_in.SI_Logged_in(self)


	def clicklogout(self):
	  	self.loginpage = Login_page.Login_page(self)

	def clickpersonaldetails(self):
		self.personaldetails = Personal_details.Personal_details(self)

	def clickaddfine(self):
		self.addfine = Add_fine.Add_fine(self)

	def checkvalidity(self):
		fineename = self.addfine.fineename_entry.get()
		fineename = str.lower(fineename)

		self.mycursor = self.database()
		self.mycursor.execute('SELECT finee_username FROM finee')
		self.finee_list = self.mycursor.fetchall()
		self.finee_list = list(sum(self.finee_list, ()))

		if fineename not in self.finee_list:
			self.signuppage = Signup_page.Signup_page(self)
		else:
			self.addfine.fineename_error.configure(text="USER EXISTS.")


	def displayfine(self):
		self.mycursor = self.database()
		self.mycursor.execute('SELECT amount FROM fine WHERE type_of_fine = "%s"'%(self.addfine.finetype.get()))
		self.otherfines = self.mycursor.fetchall()
		self.otherfines = list(sum(self.otherfines, ()))

		self.addfine.amount_entry.configure(text=self.otherfines)

	def firstfine(self):
		self.mycursor = self.database()
		self.mycursor.execute('SELECT relative_distance FROM station_coordinates WHERE station_name="%s" '%(self.addfine.fromstation.get()))
		self.f = self.mycursor.fetchall()
		self.f = list(sum(self.f, ()))
		self.mycursor.execute('SELECT relative_distance FROM station_coordinates WHERE station_name="%s" '%(self.addfine.station.get()))
		self.t = self.mycursor.fetchall()
		self.t = list(sum(self.t, ()))
		self.distance = abs(self.t[0] - self.f[0])
		self.amount = 250 + self.distance

		self.addfine.amount_entry.configure(text=self.amount)


	def clicksubmit(self):
		self.mycursor = self.database()
		finerusername = self.loginpage.username_entry.get()
		#finerid = self.mycursor.execute('SELECT finer_id FROM finer WHERE finer_username="%s"'%(self.loginpage.username_entry.get()))
		fineeusername = self.addfine.fineename_entry.get()
		#fineeid = self.mycursor.execute('SELECT finee_id from finee WHERE finee_username="%s"'%(self.addfine.fineename_entry.get()))
		fine_at = self.addfine.station.get()

		fine_type = self.addfine.finetype.get()

		if self.addfine.finetype.get()=="Travelling without ticket":
			fine_amt = self.amount
		else:
			self.mycursor.execute('SELECT amount FROM fine WHERE type_of_fine = "%s" '%(self.addfine.finetype.get()))
			amt = self.mycursor.fetchall()
			amt=list(sum(amt, ()))
			
			fine_amt = amt[0]

		self.mycursor.execute('INSERT INTO fine_generated(finer_username, finee_username, type_of_fine, fine_amt, fine_collected_at) VALUES ("%s", "%s", "%s", "%s", "%s")'%(finerusername, fineeusername, fine_type, fine_amt, fine_at))
		self.mydb.commit()
		
		#self.mycursor.execute('SELECT fine_id FROM fine WHERE fine')

		self.tc_loggedin = TC_Logged_in.TC_Logged_in(self)
		self.finedetails()

	def finedetails(self):
		self.mycursor = self.database()
		self.query1 = 'SELECT finee_username FROM fine_generated WHERE finer_username="%s" '
		self.mycursor.execute(self.query1 % self.loginpage.username_entry.get())
		self.username1 = self.mycursor.fetchall()
		self.username1 = list(sum(self.username1, ()))
		self.query2 = 'SELECT fine_collected_at FROM fine_generated WHERE finer_username="%s" '
		self.mycursor.execute(self.query2 % self.loginpage.username_entry.get())
		self.station1 = self.mycursor.fetchall()
		self.station1 = list(sum(self.station1, ()))
		self.query3 = 'SELECT fine_amt FROM fine_generated WHERE finer_username="%s" '
		self.mycursor.execute(self.query3 % self.loginpage.username_entry.get())
		self.amount1 = self.mycursor.fetchall()
		self.amount1 = list(sum(self.amount1, ()))
		# self.query4 = 'SELECT date_time FROM fine_generated WHERE finer_username="%s" '
		# self.mycursor.execute(self.query1 % self.loginpage.username_entry.get())
		# self.datetime1 = self.mycursor.fetchall()
		# self.datetime1 = list(sum(self.datetime1, ()))

		self.query5 = 'SELECT count(id) FROM fine_generated'
		#self.query1 = 'SELECT finee_username FROM fine_generated WHERE finer_username="%s" '
		self.mycursor.execute(self.query5)
		self.count = self.mycursor.fetchall()
		self.count = list(sum(self.count, ()))

		k=0.2
		for i in range(0, self.count[0]):
			j=0.35
			self.u = tk.Label(self.tc_loggedin.details_frame, text=self.username1[i], fg="black", bg="white", font=("Times", "13"))
			self.u.place(relx=j, rely=k)
			j+=0.15
			self.s = tk.Label(self.tc_loggedin.details_frame, text=self.station1[i], fg="black", bg="white", font=("Times", "13"))
			self.s.place(relx=j, rely=k)
			j+=0.15
			self.a = tk.Label(self.tc_loggedin.details_frame, text=self.amount1[i], fg="black", bg="white", font=("Times", "13"))
			self.a.place(relx=j, rely=k)
			j+=0.15
			# self.dt = tk.Label(self.tc_loggedin.details_frame, text=self.datetime1[i], fg="black", bg="white", font=("Times", "13"))
			# self.dt.place(relx=j, rely=k)
			k+=0.1

	def passengerfines(self):
		self.mycursor = self.database()
		# fineeusername = 
		# self.type = self.addfine.finetype.get()
		self.query0 = 'SELECT type_of_fine FROM fine_generated WHERE finee_username = "%s" '
		self.mycursor.execute(self.query0 % self.loginpage.username_entry.get())
		self.type = self.mycursor.fetchall()
		self.type = list(sum(self.type, ()))

		self.query1 = 'SELECT fine_collected_at FROM fine_generated WHERE finee_username = "%s" '
		self.mycursor.execute(self.query1 % self.loginpage.username_entry.get())
		self.place = self.mycursor.fetchall()
		self.place = list(sum(self.place, ()))

		self.query2 = 'SELECT fine_amt FROM fine_generated WHERE finee_username = "%s" '
		self.mycursor.execute(self.query2 % self.loginpage.username_entry.get())
		self.fineamount = self.mycursor.fetchall()
		self.fineamount = list(sum(self.fineamount, ()))

		self.mycursor.execute('SELECT count(id) FROM fine_generated WHERE finee_username = "%s" ' % self.loginpage.username_entry.get())
		self.count1 = self.mycursor.fetchall()
		self.count1 = list(sum(self.count1, ()))

		k=0.2
		for i in range(0, self.count1[0]):
			j=0.35
			self.u = tk.Label(self.passenger_loggedin.finedetails_frame, text=self.type[i], fg="black", bg="white", font=("Times", "13"))
			self.u.place(relx=j, rely=k)
			j+=0.15
			self.s = tk.Label(self.passenger_loggedin.finedetails_frame, text=self.place[i], fg="black", bg="white", font=("Times", "13"))
			self.s.place(relx=j, rely=k)
			j+=0.15
			self.a = tk.Label(self.passenger_loggedin.finedetails_frame, text=self.fineamount[i], fg="black", bg="white", font=("Times", "13"))
			self.a.place(relx=j, rely=k)
			k+=0.1



	def clickbacktc(self):
		self.tc_loggedin = TC_Logged_in.TC_Logged_in(self)
		self.finedetails()

	def clickbackpassenger(self):
		self.passenger_loggedin = Passenger_Logged_in.Passenger_Logged_in(self)


if __name__=="__main__":
	root = tk.Tk()
	r = Root(root)
	r.mainloop()