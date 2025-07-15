import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class AirlineManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Management System")
        self.root.geometry("1000x700")

        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure("TButton", padding=10, font=("calibri", 12))
        self.style.configure("TLabel", font=("calibri", 12))
        self.style.configure("TEntry", font=("calibri", 12))
        self.style.configure("TNotebook", font=("calibri", 14))
        self.style.configure("TNotebook.Tab", font=("calibri", 12))

        # Initialize database
        self.conn = sqlite3.connect('airline.db')
        self.conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key support
        self.cursor = self.conn.cursor()
        self.create_tables()
        

        # Create UI elements
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.create_flight_tab()
        self.create_passenger_tab()
        self.create_ticket_tab()
        self.create_employee_tab()
        self.create_aircraft_tab()
        self.create_airports_tab()
    

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        # Create tables if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Flights (
                FlightID INTEGER PRIMARY KEY NOT NULL,
                Origin TEXT NOT NULL,
                Destination TEXT NOT NULL,
                DepartureTime TEXT NOT NULL,
                ArrivalTime TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Passengers (
                PassengerID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL,
                Phone TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tickets (
                TicketID INTEGER PRIMARY KEY NOT NULL,
                PassengerID INTEGER NOT NULL,
                FlightID INTEGER NOT NULL,
                SeatNumber TEXT ,
                Price REAL NOT NULL,
                FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID),
                FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Airports (
                AirportID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Location TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Aircrafts (
                AircraftID INTEGER PRIMARY KEY NOT NULL,
                Type TEXT NOT NULL,
                Capacity INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Position TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_flight_tab(self):
        flight_tab = ttk.Frame(self.notebook)
        self.notebook.add(flight_tab, text='Flights')

        ttk.Label(flight_tab, text="Origin:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.origin_entry = ttk.Entry(flight_tab)
        self.origin_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(flight_tab, text="Destination:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.destination_entry = ttk.Entry(flight_tab)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(flight_tab, text="Departure Time:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.departure_entry = ttk.Entry(flight_tab)
        self.departure_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(flight_tab, text="Arrival Time:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.arrival_entry = ttk.Entry(flight_tab)
        self.arrival_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(flight_tab, text="Flight ID:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.flight_id_entry = ttk.Entry(flight_tab)
        self.flight_id_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_flight_button = ttk.Button(flight_tab, text="Add Flight", command=self.add_flight)
        self.add_flight_button.grid(row=5,column=0,columnspan=1,pady=5, padx=10,sticky="ew")

        self.view_flights_button = ttk.Button(flight_tab, text="View Flights", command=self.display_flights)
        self.view_flights_button.grid(row=5,column=1,pady=5,padx=10,sticky="ew")

        self.update_flight_button = ttk.Button(flight_tab, text="Update Flight", command=self.update_flight)
        self.update_flight_button.grid(row=6,column=0,pady=5,columnspan=1, padx=10, sticky="ew")

        self.delete_flight_button = ttk.Button(flight_tab, text="Delete Flight", command=self.delete_flight)
        self.delete_flight_button.grid(row=6,column=1,pady=5,columnspan=1, padx=10, sticky="ew")

        # Display Flight Information Frame
        self.flight_info_text = tk.Text(flight_tab, height=20, width=110)
        self.flight_info_text.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def create_passenger_tab(self):
        passenger_tab = ttk.Frame(self.notebook)
        self.notebook.add(passenger_tab, text='Passengers')

        ttk.Label(passenger_tab, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(passenger_tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(passenger_tab, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(passenger_tab)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(passenger_tab, text="Phone:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = ttk.Entry(passenger_tab)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(passenger_tab, text="Passenger ID:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.passenger_id_entry = ttk.Entry(passenger_tab)
        self.passenger_id_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_passenger_button = ttk.Button(passenger_tab, text="Add Passenger", command=self.add_passenger)
        self.add_passenger_button.grid(row=4, columnspan=1,column=0, pady=5, padx=10, sticky="ew")

        self.view_passengers_button = ttk.Button(passenger_tab, text="View Passengers", command=self.display_passengers)
        self.view_passengers_button.grid(row=4, columnspan=1,column=1, pady=5, padx=10, sticky="ew")

        self.update_passenger_button = ttk.Button(passenger_tab, text="Update Passenger", command=self.update_passenger)
        self.update_passenger_button.grid(row=5, columnspan=1, column=0,pady=10, padx=10, sticky="ew")

        self.delete_passenger_button = ttk.Button(passenger_tab, text="Delete Passenger", command=self.delete_passenger)
        self.delete_passenger_button.grid(row=5, columnspan=1,column=1, pady=10, padx=10, sticky="ew")

        # Display Passenger Information Frame
        self.passenger_info_text = tk.Text(passenger_tab, height=20, width=90)
        self.passenger_info_text.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    def create_ticket_tab(self):
        ticket_tab = ttk.Frame(self.notebook)
        self.notebook.add(ticket_tab, text='Tickets')

        ttk.Label(ticket_tab, text="Passenger ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.ticket_passenger_id_entry = ttk.Entry(ticket_tab)
        self.ticket_passenger_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(ticket_tab, text="Flight ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ticket_flight_id_entry = ttk.Entry(ticket_tab)
        self.ticket_flight_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(ticket_tab, text="Seat Number:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.seat_number_entry = ttk.Entry(ticket_tab)
        self.seat_number_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(ticket_tab, text="Price:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = ttk.Entry(ticket_tab)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_ticket_button = ttk.Button(ticket_tab, text="Add Ticket", command=self.add_ticket)
        self.add_ticket_button.grid(row=4,column=0, columnspan=1, pady=5, padx=10, sticky="ew")

        self.view_tickets_button = ttk.Button(ticket_tab, text="View Tickets", command=self.display_tickets)
        self.view_tickets_button.grid(row=4,column=1, columnspan=1, pady=5, padx=10, sticky="ew")


        # Display Ticket Information Frame
        self.ticket_info_text = tk.Text(ticket_tab, height=20, width=90)
        self.ticket_info_text.grid(row=5, column=0, columnspan=1, pady=10, padx=10)

    def create_airports_tab(self):
        airport_tab = ttk.Frame(self.notebook)
        self.notebook.add(airport_tab, text='Airports')

        # Entry fields
        ttk.Label(airport_tab, text="AirportID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.airport_name_entry = ttk.Entry(airport_tab)
        self.airport_name_entry.grid(row=0,padx=10, pady=5)

        ttk.Label(airport_tab, text="Name:").grid(row=1,padx=10, pady=5, sticky="w")
        self.airport_name_entry = ttk.Entry(airport_tab)
        self.airport_name_entry.grid(row=1,padx=10, pady=5)

        ttk.Label(airport_tab, text="Location:").grid(row=2,padx=10, pady=5, sticky="w")
        self.airport_location_entry = ttk.Entry(airport_tab)
        self.airport_location_entry.grid(row=2,padx=10, pady=5)

        # Buttons
        self.add_airport_button = ttk.Button(airport_tab, text="Add Airport", command=self.add_airport)
        self.add_airport_button.grid(row=3,column=0, columnspan=1, pady=5, padx=10, sticky="ew")

        self.display_airports_button = ttk.Button(airport_tab, text="View Airports", command=self.display_airports)
        self.display_airports_button.grid(row=3,column=1, columnspan=1, pady=5, padx=10, sticky="ew")

        # Display Airport Information Frame
        self.airport_info_text = tk.Text(airport_tab, height=20, width=95)
        self.airport_info_text.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    def create_employee_tab(self):
        employee_tab = ttk.Frame(self.notebook)
        self.notebook.add(employee_tab, text='Employees')

        ttk.Label(employee_tab, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.employee_name_entry = ttk.Entry(employee_tab)
        self.employee_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(employee_tab, text="Position:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.employee_position_entry = ttk.Entry(employee_tab)
        self.employee_position_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(employee_tab, text="Employee ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.employee_id_entry = ttk.Entry(employee_tab)
        self.employee_id_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_employee_button = ttk.Button(employee_tab, text="Add Employee", command=self.add_employee)
        self.add_employee_button.grid(row=3,column=0,columnspan=1, pady=5, padx=10, sticky="ew")

        self.display_employees_button = ttk.Button(employee_tab, text="View Employees", command=self.display_employees)
        self.display_employees_button.grid(row=3,column=1,columnspan=1, pady=5, padx=10, sticky="ew")


        # Display Employee Information Frame
        self.employee_info_text = tk.Text(employee_tab, height=20, width=90)
        self.employee_info_text.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def create_aircraft_tab(self):
        aircraft_tab = ttk.Frame(self.notebook)
        self.notebook.add(aircraft_tab, text='Aircrafts')

        ttk.Label(aircraft_tab, text="Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.aircraft_type_entry = ttk.Entry(aircraft_tab)
        self.aircraft_type_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(aircraft_tab, text="Capacity:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.capacity_entry = ttk.Entry(aircraft_tab)
        self.capacity_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(aircraft_tab, text="Aircraft ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.aircraft_id_entry = ttk.Entry(aircraft_tab)
        self.aircraft_id_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_aircraft_button = ttk.Button(aircraft_tab, text="Add Aircraft", command=self.add_aircraft)
        self.add_aircraft_button.grid(row=3,column=0,columnspan=1, pady=5, padx=5, sticky="ew")
        
        self.display_aircrafts_button = ttk.Button(aircraft_tab, text="View Aircrafts", command=self.display_aircrafts)
        self.display_aircrafts_button.grid(row=3,column=1,columnspan=1, pady=5, padx=10, sticky="ew")
        # Display Aircraft Information Frame
        self.aircraft_info_text = tk.Text(aircraft_tab, height=20, width=90)
        self.aircraft_info_text.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def add_flight(self):
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        departure_time = self.departure_entry.get()
        arrival_time = self.arrival_entry.get()

        if origin == "" or destination == "" or departure_time == "" or arrival_time == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Flights (Origin, Destination, DepartureTime, ArrivalTime) VALUES (?, ?, ?, ?)",
                            (origin, destination, departure_time, arrival_time))
        self.conn.commit()
        self.display_flights()
        messagebox.showinfo("Success", "Flight added successfully")

    def add_passenger(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if name == "" or email == "" or phone == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Passengers (Name, Email, Phone) VALUES (?, ?, ?)", (name, email, phone))
        self.conn.commit()
        self.display_passengers()
        messagebox.showinfo("Success", "Passenger added successfully")

    def add_airport(self):
        name = self.airport_name_entry.get()
        location = self.airport_location_entry.get()

        if name == "" or location == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Airports (Name, Location) VALUES (?, ?)", (name, location))
        self.conn.commit()
        self.display_airports()
        messagebox.showinfo("Success", "Airport added successfully")

    def add_ticket(self):
        passenger_id = self.ticket_passenger_id_entry.get()
        flight_id = self.ticket_flight_id_entry.get()
        seat_number = self.seat_number_entry.get()
        price = self.price_entry.get()

        if passenger_id == "" or flight_id == "" or price == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Tickets (PassengerID, FlightID, SeatNumber, Price) VALUES (?, ?, ?, ?)",
                            (passenger_id, flight_id, seat_number, price))
        self.conn.commit()
        self.display_tickets()
        messagebox.showinfo("Success", "Ticket added successfully")

    def display_airports(self):
        self.airport_info_text.delete(1.0, tk.END)
        airports = self.cursor.execute("SELECT * FROM Airports").fetchall()
        for airport in airports:
            self.airport_info_text.insert(tk.END, f"Airport ID: {airport[0]}, Name: {airport[1]}, Location: {airport[2]}\n")

    def add_employee(self):
        name = self.employee_name_entry.get()
        position = self.employee_position_entry.get()

        if name == "" or position == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Employees (Name, Position) VALUES (?, ?)", (name, position))
        self.conn.commit()
        self.display_employees()
        messagebox.showinfo("Success", "Employee added successfully")

    def add_aircraft(self):
        aircraft_type = self.aircraft_type_entry.get()
        capacity = self.capacity_entry.get()

        if aircraft_type == "" or capacity == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Aircrafts (Type, Capacity) VALUES (?, ?)", (aircraft_type, capacity))
        self.conn.commit()
        self.display_aircrafts()
        messagebox.showinfo("Success", "Aircraft added successfully")

    def display_flights(self):
        self.flight_info_text.delete(1.0, tk.END)
        flights = self.cursor.execute("SELECT * FROM Flights").fetchall()
        for flight in flights:
            self.flight_info_text.insert(tk.END, f"Flight ID: {flight[0]}, Origin: {flight[1]}, Destination: {flight[2]}, Departure Time: {flight[3]}, Arrival Time: {flight[4]}\n")

    def display_passengers(self):
        self.passenger_info_text.delete(1.0, tk.END)
        passengers = self.cursor.execute("SELECT * FROM Passengers").fetchall()
        for passenger in passengers:
            self.passenger_info_text.insert(tk.END, f"Passenger ID: {passenger[0]}, Name: {passenger[1]}, Email: {passenger[2]}, Phone: {passenger[3]}\n")

    def display_tickets(self):
        self.ticket_info_text.delete(1.0, tk.END)
        tickets = self.cursor.execute("SELECT * FROM Tickets").fetchall()
        for ticket in tickets:
            self.ticket_info_text.insert(tk.END, f"Ticket ID: {ticket[0]}, Passenger ID: {ticket[1]}, Flight ID: {ticket[2]}, Seat Number: {ticket[3]}, Price: {ticket[4]}\n")

    def display_employees(self):
        self.employee_info_text.delete(1.0, tk.END)
        employees = self.cursor.execute("SELECT * FROM Employees").fetchall()
        for employee in employees:
            self.employee_info_text.insert(tk.END, f"Employee ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}\n")

    def display_aircrafts(self):
        self.aircraft_info_text.delete(1.0, tk.END)
        aircrafts = self.cursor.execute("SELECT * FROM Aircrafts").fetchall()
        for aircraft in aircrafts:
            self.aircraft_info_text.insert(tk.END, f"Aircraft ID: {aircraft[0]}, Type: {aircraft[1]}, Capacity: {aircraft[2]}\n")

    def update_flight(self):
        flight_id = self.flight_id_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        departure_time = self.departure_entry.get()
        arrival_time = self.arrival_entry.get()

        if flight_id == "" or origin == "" or destination == "" or departure_time == "" or arrival_time == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("UPDATE Flights SET Origin=?, Destination=?, DepartureTime=?, ArrivalTime=? WHERE FlightID=?",
                            (origin, destination, departure_time, arrival_time, flight_id))
        self.conn.commit()
        self.display_flights()
        messagebox.showinfo("Success", "Flight updated successfully")

    def update_passenger(self):
        passenger_id = self.passenger_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if passenger_id == "" or name == "" or email == "" or phone == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("UPDATE Passengers SET Name=?, Email=?, Phone=? WHERE PassengerID=?",
                            (name, email, phone, passenger_id))
        self.conn.commit()
        self.display_passengers()
        messagebox.showinfo("Success", "Passenger updated successfully")

    def delete_flight(self):
        flight_id = self.flight_id_entry.get()
        if flight_id == "":
            messagebox.showerror("Error", "Please enter Flight ID")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this flight?")
        if confirm:
            self.cursor.execute("DELETE FROM Flights WHERE FlightID=?", (flight_id,))
            self.conn.commit()
            self.display_flights()
            messagebox.showinfo("Success", "Flight deleted successfully")

    def delete_passenger(self):
        passenger_id = self.passenger_id_entry.get()
        if passenger_id == "":
            messagebox.showerror("Error", "Please enter Passenger ID")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this passenger?")
        if confirm:
            self.cursor.execute("DELETE FROM Passengers WHERE PassengerID=?", (passenger_id,))
            self.conn.commit()
            self.display_passengers()
            messagebox.showinfo("Success", "Passenger deleted successfully")


root = tk.Tk()
app = AirlineManagementSystem(root)
root.mainloop()
