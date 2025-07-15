import tkinter as tk
from tkinter import ttk
import sqlite3

class AirlineManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Management System")
        
        # Connect to the database
        self.conn = sqlite3.connect("airline.db")
        self.cur = self.conn.cursor()

        # Create tables if not exists
        self.create_tables()

        # Create GUI elements
        self.create_gui()

    def create_tables(self):
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Flights (
                FlightID INTEGER PRIMARY KEY NOT NULL,
                DepartureDate DATE NOT NULL,
                ArrivalDate DATE NOT NULL,
                DepartureCity TEXT,
                DestinationCity TEXT,
                DepartureTime TEXT,
                ArrivalTime TEXT
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Aircrafts (
                AircraftID INTEGER PRIMARY KEY NOT NULL,
                Model TEXT,
                Capacity INTEGER
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Passengers (
                PassengerID INTEGER PRIMARY KEY NOT NULL,
                Passengerage INTEGER,
                Name TEXT,
                Contact TEXT,
                Passport_number INTEGER UNIQUE,
                passenger_email TEXT NOT NULL UNIQUE,
                FlightID INTEGER NOT NULL,         
                FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Bookings(
                Booking_id INTEGER PRIMARY KEY,
                FlightID INTEGER NOT NULL,
                PassengerID INTEGER NOT NULL,
                FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
                FOREIGN KEY(PassengerID) REFERENCES Passengers(PassengerID)        
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Crews (
                CrewID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Role TEXT NOT NULL
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Airports (
                AirportID INTEGER PRIMARY KEY,
                Name TEXT,
                Location TEXT
            )
        """)
        self.conn.commit()

    def create_gui(self):
        # Add Flight

        self.departure_date_label = ttk.Label(self.root, text="Departure Date:")
        self.departure_date_label.grid(row=0, column=0, padx=5, pady=5)
        self.departure_date_entry = ttk.Entry(self.root)
        self.departure_date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.departure_city_label = ttk.Label(self.root, text="Departure City:")
        self.departure_city_label.grid(row=2, column=0, padx=5, pady=5)
        self.departure_city_entry = ttk.Entry(self.root)
        self.departure_city_entry.grid(row=2, column=1, padx=5, pady=5)

        self.departure_time_label = ttk.Label(self.root, text="Departure Time:")
        self.departure_time_label.grid(row=3, column=0, padx=5, pady=5)
        self.departure_time_entry = ttk.Entry(self.root)
        self.departure_time_entry.grid(row=3, column=1, padx=5, pady=5)
       
        self.destination_city_label = ttk.Label(self.root, text="Destination city:")
        self.destination_city_label.grid(row=4, column=0, padx=5, pady=5)
        self.destination_city_entry = ttk.Entry(self.root)
        self.destination_city_entry.grid(row=4, column=1, padx=5, pady=5)

        self.arrival_date_label = ttk.Label(self.root, text="Arrival Date:")
        self.arrival_date_label.grid(row=5, column=0, padx=5, pady=5)
        self.arrival_date_entry = ttk.Entry(self.root)
        self.arrival_date_entry.grid(row=5, column=1, padx=5, pady=5)

        self.arrival_time_label = ttk.Label(self.root, text="Arrival Time:")
        self.arrival_time_label.grid(row=6, column=0, padx=5, pady=5)
        self.arrival_time_entry = ttk.Entry(self.root)
        self.arrival_time_entry.grid(row=6, column=1, padx=5, pady=5)

        self.passenger_name_label = ttk.Label(self.root, text="Passenger Name:")
        self.passenger_name_label.grid(row=7, column=0, padx=5, pady=5)
        self.passenger_name_entry = ttk.Entry(self.root)
        self.passenger_name_entry.grid(row=7, column=1, padx=5, pady=5)

        self.mobile_number_label = ttk.Label(self.root, text="Mobile Number:")
        self.mobile_number_label.grid(row=8, column=0, padx=5, pady=5)
        self.mobile_number_entry = ttk.Entry(self.root)
        self.mobile_number_entry.grid(row=8, column=1, padx=5, pady=5)

        self.passenger_age_label=ttk.Label(self.root,text="Passenger Age")
        self.passenger_age_label.grid(row=9,column=0,padx=5,pady=5)
        self.passenger_age_entry=ttk.Entry(self.root)
        self.passenger_age_entry.grid(row=9, column=1, padx=5, pady=5)

        self.passport_number_label=ttk.Label(self.root,text="Passport Number")
        self.passport_number_label.grid(row=10,column=0,padx=5,pady=5)
        self.passport_number_entry=ttk.Entry(self.root)
        self.passport_number_entry.grid(row=10,column=1,padx=5,pady=5)

        self.passenger_email_label=ttk.Label(self.root,text="Passenger Email")
        self.passenger_email_label.grid(row=11,column=0,padx=5,pady=5)
        self.passenger_email_entry=ttk.Entry(self.root)
        self.passenger_email_entry.grid(row=11,column=1,padx=5,pady=5)
    
        
        self.add_flight_button = ttk.Button(self.root, text="Add Flight", command=self.add_flight)
        self.add_flight_button.grid(row=12, column=0,padx=5, pady=5)

        # Delete Flight
        self.delete_flight_button = ttk.Button(self.root, text="Delete Flight", command=self.delete_flight)
        self.delete_flight_button.grid(row=12, column=1,padx=5, pady=5)

        # Update Flight
        self.update_flight_button = ttk.Button(self.root, text="Update Flight", command=self.update_flight)
        self.update_flight_button.grid(row=12, column=2,padx=5, pady=5)

        #Add Passenger
        self.add_passenger_button=ttk.Button(self.root,text="Add Passenger",command=self.add_passenger)
        self.add_passenger_button.grid(row=13, column=0,padx=5, pady=5)
        
        #update passenger
        self.update_passenger_button=ttk.Button(self.root,text="Update Passenger",command=self.update_passenger)
        self.update_passenger_button.grid(row=13,column=1,padx=5, pady=5)
        # Add more GUI elements for Aircrafts, Passengers, Tickets, Crews, and Airports
        #delete passenger
        self.delete_passenger_button = ttk.Button(self.root, text="Delete Passenger", command=self.delete_passenger)
        self.delete_passenger_button.grid(row=13, column=2,padx=5, pady=5)

    def add_flight(self):
        departure_city = self.departure_city_entry.get()
        destination_city = self.destination_city_entry.get()
        departure_time = self.departure_time_entry.get()
        arrival_time = self.arrival_time_entry.get()
        departure_date=self.departure_date_entry.get()
        arrival_date=self.arrival_date_entry.get()




        self.cur.execute("INSERT INTO Flights (DepartureDate,ArrivalDate,DepartureCity, DestinationCity, DepartureTime, ArrivalTime) VALUES (?, ?, ?, ?,?,?)",
                         (departure_date,arrival_date,departure_city, destination_city, departure_time, arrival_time))
        self.conn.commit()
        print("Flight added successfully.")

    def add_passenger(self):
        passenger_name=self.passenger_name_entry.get()
        mobile_number=self.mobile_number_entry.get()
        passenger_age=self.passenger_age_entry.get()
        passport_number=self.passport_number_entry.get()
        passenger_email=self.passenger_email_entry.get()


        self.cur.execute("INSERT INTO Passengers (Passengerage,Name,Contact,Passport_number,passenger_email) VALUES (?,?,?,?,?)", 
                         (passenger_age,passenger_name,mobile_number,passport_number,passenger_email))
        self.conn.commit()
        print("Passenger details added successfully.")


    def delete_flight(self):
        # Get flight ID from user
        flight_id = int(input("Enter Flight ID to delete: "))

        # Delete flight record from the database
        self.cur.execute("DELETE FROM Flights WHERE FlightID=?", (flight_id,))
        self.conn.commit()
        print("Flight deleted successfully.")

    def delete_passenger(self):
        passenger_id=int(input("Enter passenger_id to delete:"))
        self.cur.execute("DELETE FROM Passengers WHERE PassengerID=?",(passenger_id,))
        self.conn.commit()
        print("passenger deleted successfully.")

    def update_flight(self):
        # Get flight ID from user
        flight_id = int(input("Enter Flight ID to update: "))

        # Get new values from user
        departure_city = input("Enter new departure city: ")
        destination_city = input("Enter new destination city: ")
        departure_time = input("Enter new departure time: ")
        arrival_time = input("Enter new arrival time: ")
        departure_date=input("enter new departure date: ")
        arrival_date=input("enter new arrival date:")

        # Update flight record in the database
        self.cur.execute("UPDATE Flights SET DepartureCity=?, DestinationCity=?, DepartureTime=?, ArrivalTime=?,DepartureDate=?,ArrivalDate=? WHERE FlightID=?",
                         (departure_city, destination_city, departure_time, arrival_time,departure_date,arrival_date,flight_id))
        self.conn.commit()
        print("Flight updated successfully.")

    def update_passenger(self):
        passenger_id=int(input("Enter passenger id to update: "))
        passenger_name=input("Enter new passenger name: ")
        mobile_number=input("Enter new mobile number: ")
        passenger_age=input("enter new passengers age: ")
        passport_number=input("enter new passport number: ")
        passenger_email=input("enter new passenger email: ")
        self.cur.execute("UPDATE Passengers SET Name=?,Contact=?,Passengerage=?,Passport_number=?,passenger_email=? WHERE  PassengerID=?",
                         (passenger_name,mobile_number,passenger_age,passport_number,passenger_email,passenger_id))
        self.conn.commit()
        print("passenger updated successfully")

    

    # Implement similar functions for Aircrafts, Passengers, Tickets, Crews, and Airports


if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineManagementSystem(root)
    root.mainloop()
