import tkinter as tk
import tkcalendar
# import TC_Logged_in

class Add_fine(tk.Frame):
	def __init__(self,master):

		self.master = master
		main_frame = tk.Frame(master.canvas, bg="white")
		main_frame.place(relheight=1, relwidth=1)

		title_frame = tk.Frame(main_frame, bg="#003145", bd=13)
		title_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

		title_label = tk.Label(title_frame, text="RAILWAY FINE SYSTEM", font=("Comic Sans MS", "62"), bg="#003145", fg="white", )
		title_label.place(relheight=1, relwidth=1)

		self.fine_frame = tk.Frame(main_frame, bg="white")
		self.fine_frame.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.6)

		name_label = tk.Label(self.fine_frame, bg="white", text="Name of finee: ", fg="black", font=("Helvetica", "17"))
		name_label.place(relx=0.05, rely=0.05)
		self.fineename_entry = tk.Entry(self.fine_frame)
		self.fineename_entry.place(relx=0.2, rely=0.05)

		check_button = tk.Button(self.fine_frame, bg="white", fg="black", text="Check Validity", command=master.checkvalidity)
		check_button.place(relx=0.7, rely=0.05)

		self.fineename_error = tk.Label(self.fine_frame, bg="white", fg="red", text="")
		self.fineename_error.place(relx=0.5, rely=0.075)

		station_label = tk.Label(self.fine_frame, bg="white", fg="black", text="Place: ", font=("Helvetica", "17"))
		station_label.place(relx=0.05, rely=0.15)

		self.station = tk.StringVar(self.fine_frame)
		self.stations = ("Chhatrapati Shivaji Maharaj Terminus", "Sandhurst Road", "Byculla", "Currey Road", "Dadar", "Matunga", "Sion", "Kurla",
					"Vidyavihar", "Ghatkopar", "Vikhroli", "Kanjurmarg", "Bhandup", "Nahur", "Mulund", "Thane", "Kalwa", "Mumbra", "Diva",
					"Kopar", "Dombivali", "Kalyan", "Vithalwadi", "Ulhasnagar", "Ambernath", "Badlapur", "Vangani", "Neral", "Karjat",
					"Khopoli")
		self.station_option = tk.OptionMenu(self.fine_frame, self.station, *self.stations)
		self.station_option.place(relx=0.2, rely=0.15, width=200)
		self.station.set("Select station")

		finetype_label = tk.Label(self.fine_frame, bg="white", fg="black", text="Fine type: ", font=("Helvetica", "17"))
		finetype_label.place(relx=0.05, rely=0.35)

		self.finetype = tk.StringVar(self.fine_frame)
		choices = ("Travelling without ticket", "Travelling Fraudulently", "Alarm chain pulling", "Travelling in coach reserved for handicapped",
					"Travelling on roof top", "Trespassing", "Nuisance and littering", "Bill pasting", "Touting", "Unauthorised Hawking")
		self.finetype_option = tk.OptionMenu(self.fine_frame, self.finetype, *choices, command=self.places)
		self.finetype_option.place(relx=0.2, rely=0.35, width=300)
		self.finetype.set("Select your fine type")


	def places(self,master):
		if self.finetype.get()=="Travelling without ticket":
			blank_frame = tk.Frame(self.fine_frame, bg="white")
			blank_frame.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.4)

			from_label = tk.Label(self.fine_frame, text="From station:   ", bg="white", font=("Helvetica", "13"))
			from_label.place(relx=0.1, rely=0.45)
			self.fromstation = tk.StringVar(self.fine_frame)
			self.fromstation_option = tk.OptionMenu(self.fine_frame, self.fromstation, *self.stations, command=self.fromto)
			self.fromstation_option.place(relx=0.2, rely=0.45)
			self.fromstation.set("Select station")

			self.to_label = tk.Label(self.fine_frame, text="To station:    ", bg="white", font=("Helvetica", "13"))
			self.to_label.place(relx=0.1, rely=0.55)
			self.to_entry = tk.Label(self.fine_frame, text=self.station.get(), bg="white", fg="black", font=("Helvetica", "13"))
			self.to_entry.place(relx=0.2, rely=0.55)
		else:
			blank_frame = tk.Frame(self.fine_frame, bg="white")
			blank_frame.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.4)

			amount_label = tk.Label(self.fine_frame, bg="white", fg="black", text="Fine Amount: ", font=("Helvetica", "17"))
			amount_label.place(relx=0.05, rely=0.55)

			self.amount_entry = tk.Label(self.fine_frame, text="", fg="black", bg="white", font=("Helvetica", "17"))
			self.amount_entry.place(relx=0.2, rely=0.55)

			self.master.displayfine()

			self.submit_button = tk.Button(self.fine_frame, text="Next >", bg="white", fg="black", width=20, font=("Helvetica", "13"), command=self.master.clicksubmit)
			self.submit_button.place(relx=0.5, rely=0.8)


	def fromto(self,master):
		amount_label = tk.Label(self.fine_frame, bg="white", fg="black", text="Fine Amount: ", font=("Helvetica", "17"))
		amount_label.place(relx=0.05, rely=0.65)

		self.amount_entry = tk.Label(self.fine_frame, text="", fg="black", bg="white", font=("Helvetica", "17"))
		self.amount_entry.place(relx=0.2, rely=0.65)

		self.master.firstfine()

		self.submit_button = tk.Button(self.fine_frame, text="Next >", bg="white", fg="black", width=20, font=("Helvetica", "13"), command=self.master.clicksubmit)
		self.submit_button.place(relx=0.5, rely=0.8)

		