# ✈️ Airline Management System

This project is a **GUI-based Airline Management System** developed in **Python using Tkinter** and **SQLite3**. It enables airline staff to manage essential operations such as flights, passengers, bookings, aircrafts, airports, employees, and crew members.

---

## 🛠 Features

- **Flight Management**
  - Add, update, delete, and view flight details
  - Capture details like departure/arrival cities, dates, and times

- **Passenger Management**
  - Register passengers with name, contact, age, passport, and email
  - Edit and remove existing passenger records

- **Booking System**
  - Book tickets linking passengers to flights
  - Auto-generate booking IDs

- **Aircraft and Airport Management**
  - Add and display aircraft types and capacities
  - Manage airports with name and location info

- **Employee & Crew Management**
  - Manage employee and crew member records with roles

- **GUI Interface**
  - Built with `Tkinter` for interactive data entry and display
  - Organized tabs for different modules

---

## 🗂 Project Structure

```
dbms project/
├── main.py                         # Primary script to launch the system
├── airline.db                      # SQLite database file
├── py/
│   ├── airr.py                     # Additional airline logic (GUI/DB)
│   ├── Bookmanagement system.py    # Book management code
│   └── python/
│       ├── air.py, duplicate.py    # Main logic and duplicate GUI
│       ├── __pycache__/            # Compiled bytecode
│       └── .vscode/                # Editor config
├── .git/                           # Git versioning data
```

---

## 💾 Technologies Used

- **Python 3**
- **SQLite3** (for lightweight DB)
- **Tkinter** (for GUI)
- **Object-Oriented Programming** for system modularity

---

## 🚀 Getting Started

1. **Install Python 3**
2. Run the app:
   ```bash
   python main.py
   ```
3. Make sure `airline.db` is in the same directory or created on first run.
