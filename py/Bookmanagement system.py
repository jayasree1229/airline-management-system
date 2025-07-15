import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class BookManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1000x700")

        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure("TButton", padding=10, font=("calibri", 12))
        self.style.configure("TLabel", font=("calibri", 12))
        self.style.configure("TEntry", font=("calibri", 12))
        self.style.configure("TNotebook", font=("calibri", 14))
        self.style.configure("TNotebook.Tab", font=("calibri", 12))

        # Initialize database
        self.conn = sqlite3.connect('bookss.db')
        self.conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key support
        self.cursor = self.conn.cursor()
        self.create_tables()
        

        # Create UI elements
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.create_books_tab()
        self.create_authors_tab()
        self.create_genres_tab()
        self.create_publishers_tab()
        

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        # Create tables if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                bookid INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                authorid INTEGER NOT NULL,
                genreid INTEGER NOT NULL,
                publisherid INTEGER NOT NULL,
                year INTEGER NOT NULL,
                FOREIGN KEY (authorid) REFERENCES Authors(authorid),
                FOREIGN KEY (genreid) REFERENCES Genres(genreid),
                FOREIGN KEY (publisherid) REFERENCES Publishers(publisherid)
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Authors (
                authorid INTEGER PRIMARY KEY AUTOINCREMENT,
                authorname TEXT NOT NULL,
                biography TEXT NOT NULL
                
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Genres (
                genreid INTEGER PRIMARY KEY AUTOINCREMENT,
                genrename TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Publishers(
                publisherid INTEGER PRIMARY KEY AUTOINCREMENT,
                publishername TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_books_tab(self):
        books_tab = ttk.Frame(self.notebook)
        self.notebook.add(books_tab, text='Books')

        ttk.Label(books_tab, text="Bookid:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.bookid_entry = ttk.Entry(books_tab)
        self.bookid_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(books_tab, text="title:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.title_entry = ttk.Entry(books_tab)
        self.title_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(books_tab, text="authorid:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.author_id_entry = ttk.Entry(books_tab)
        self.author_id_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(books_tab, text="genreid:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.genre_id_entry = ttk.Entry(books_tab)
        self.genre_id_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(books_tab, text="publisherid:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.publisher_id_entry = ttk.Entry(books_tab)
        self.publisher_id_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(books_tab, text="Year:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.year_entry = ttk.Entry(books_tab)
        self.year_entry.grid(row=5, column=1, padx=10, pady=5)

        self.add_books_button = ttk.Button(books_tab, text="Add book", command=self.add_books)
        self.add_books_button.grid(row=6,column=0,columnspan=1,pady=5, padx=10,sticky="ew")

        self.view_books_button = ttk.Button(books_tab, text="View books", command=self.display_books)
        self.view_books_button.grid(row=6,column=1,pady=5,padx=10,sticky="ew")

        self.update_books_button = ttk.Button(books_tab, text="Update books", command=self.update_books)
        self.update_books_button.grid(row=7,column=0,pady=5,columnspan=1, padx=10, sticky="ew")

        self.delete_books_button = ttk.Button(books_tab, text="Delete books", command=self.delete_books)
        self.delete_books_button.grid(row=7,column=1,pady=5,columnspan=1, padx=10, sticky="ew")

        # Display Flight Information Frame
        self.books_info_text = tk.Text(books_tab, height=20, width=110)
        self.books_info_text.grid(row=8, column=0, columnspan=2, pady=10, padx=10)

    def create_authors_tab(self):
        authors_tab = ttk.Frame(self.notebook)
        self.notebook.add(authors_tab, text='Authors')

        ttk.Label(authors_tab, text="authorid:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.authorid_entry = ttk.Entry(authors_tab)
        self.authorid_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(authors_tab, text="authorname:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.authorname_entry = ttk.Entry(authors_tab)
        self.authorname_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(authors_tab, text="biography:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.biography_entry = ttk.Entry(authors_tab)
        self.biography_entry.grid(row=2, column=1, padx=10, pady=5)

       
        self.add_authors_button = ttk.Button(authors_tab, text="Add author", command=self.add_authors)
        self.add_authors_button.grid(row=3, columnspan=1,column=0, pady=5, padx=10, sticky="ew")

        self.view_authors_button = ttk.Button(authors_tab, text="View authors", command=self.display_authors)
        self.view_authors_button.grid(row=3, columnspan=1,column=1, pady=5, padx=10, sticky="ew")

        self.update_authors_button = ttk.Button(authors_tab, text="Update author", command=self.update_authors)
        self.update_authors_button.grid(row=4, columnspan=1, column=0,pady=10, padx=10, sticky="ew")

        self.delete_authors_button = ttk.Button(authors_tab, text="Delete author", command=self.delete_authors)
        self.delete_authors_button.grid(row=4, columnspan=1,column=1, pady=10, padx=10, sticky="ew")

        # Display Passenger Information Frame
        self.authors_info_text = tk.Text(authors_tab, height=20, width=90)
        self.authors_info_text.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def create_genres_tab(self):
        genres_tab = ttk.Frame(self.notebook)
        self.notebook.add(genres_tab, text='Genres')

        ttk.Label(genres_tab, text="genre ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.genreid_entry = ttk.Entry(genres_tab)
        self.genreid_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(genres_tab, text="genre name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.genrename_entry = ttk.Entry(genres_tab)
        self.genrename_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_genre_button = ttk.Button(genres_tab, text="Add genre", command=self.add_genres)
        self.add_genre_button.grid(row=4,column=0, columnspan=1, pady=5, padx=10, sticky="ew")

        self.view_genre_button = ttk.Button(genres_tab, text="View genres", command=self.display_genres)
        self.view_genre_button.grid(row=4,column=1, columnspan=1, pady=5, padx=10, sticky="ew")


        # Display Ticket Information Frame
        self.genre_info_text = tk.Text(genres_tab, height=20, width=90)
        self.genre_info_text.grid(row=5, column=0, columnspan=1, pady=10, padx=10)

    def create_publishers_tab(self):
        publishers_tab = ttk.Frame(self.notebook)
        self.notebook.add(publishers_tab, text='publishers')

        # Entry fields
        ttk.Label(publishers_tab, text="publisherid:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.publisherid_entry = ttk.Entry(publishers_tab)
        self.publisherid_entry.grid(row=0,padx=10, pady=5)

        ttk.Label(publishers_tab, text="publishersname:").grid(row=1,padx=10, pady=5, sticky="w")
        self.publishername_entry = ttk.Entry(publishers_tab)
        self.publishername_entry.grid(row=1,padx=10, pady=5)


        # Buttons
        self.add_publishers_button = ttk.Button(publishers_tab, text="Add publisher", command=self.add_publishers)
        self.add_publishers_button.grid(row=3,column=0, columnspan=1, pady=5, padx=10, sticky="ew")

        self.display_publishers_button = ttk.Button(publishers_tab, text="View publishers", command=self.display_publishers)
        self.display_publishers_button.grid(row=3,column=1, columnspan=1, pady=5, padx=10, sticky="ew")

        # Display Airport Information Frame
        self.publishers_info_text = tk.Text(publishers_tab, height=20, width=95)
        self.publishers_info_text.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    

    def add_books(self):
        bookid = self.bookid_entry.get()
        title = self.title_entry.get()
        authorid = self.author_id_entry.get()
        genreid = self.genre_id_entry.get()
        publisherid=self.publisher_id_entry.get()
        year=self.year_entry.get()

        if bookid == "" or title == "" or authorid == "" or genreid == "" or publisherid == "" or year == "":
            messagebox.showerror("Error","Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Books (bookid,title,authorid,genreid,publisherid,year) VALUES (?,?,?,?,?,?)",
                            (bookid,title,authorid,genreid,publisherid,year))
        self.conn.commit()
        self.display_books()
        messagebox.showinfo("Success", "Books added successfully")

    def add_authors(self):
        authorid= self.authorid_entry.get()
        authorname= self.authorname_entry.get()
        biography= self.biography_entry.get()

        if authorid== "" or authorname == "" or biography == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Authors (authorid,authorname,biography) VALUES (?, ?, ?)", (authorid,authorname,biography))
        self.conn.commit()
        self.display_authors()
        messagebox.showinfo("Success", "Passenger added successfully")

    def add_genres(self):
        genreid = self.genreid_entry.get()
        genrename = self.genrename_entry.get()

        if genreid == "" or genrename == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("INSERT INTO Genres (genreid,genrename) VALUES (?, ?)", (genreid,genrename))
        self.conn.commit()
        self.display_genres()
        messagebox.showinfo("Success", "genre added successfully")

    def add_publishers(self):
        publisherid=self.publisherid_entry.get()
        publishername=self.publishername_entry.get()

        if publisherid=="" or publishername=="":
            messagebox.showerror("Error","please fill in all fields")
            return
        self.cursor.execute("INSERT INTO Publishers(publisherid,publishername) VALUES(?,?)",(publisherid,publishername))
        self.conn.commit()
        self.display_publishers()
        messagebox.showinfo("Success","publisher added successfully")

    def display_genres(self):
        self.genre_info_text.delete(1.0, tk.END)
        Genres = self.cursor.execute("SELECT * FROM Genres").fetchall()
        for genre in Genres:
            self.genre_info_text.insert(tk.END, f"genreid: {genre[0]}, genrename: {genre[1]}\n")
    
    def display_publishers(self):
        self.publishers_info_text.delete(1.0,tk.END)
        publishers=self.cursor.execute("SELECT * FROM Publishers").fetchall()
        for publisher in publishers:
            self.publishers_info_text.insert(tk.END,f"publisherid:{publisher[0]},publishername:{publisher[1]}\n")

    

    

    def display_books(self):
        self.books_info_text.delete(1.0, tk.END)
        Books = self.cursor.execute("SELECT * FROM Books").fetchall()
        for book in Books:
            self.books_info_text.insert(tk.END, f"bookid: {book[0]}, title: {book[1]}, authorid: {book[2]}, genreid: {book[3]}, publisherid: {book[4]}, year:{book[5]}\n")

    def display_authors(self):
        self.authors_info_text.delete(1.0, tk.END)
        authors = self.cursor.execute("SELECT * FROM Authors").fetchall()
        for author in authors:
            self.authors_info_text.insert(tk.END, f"authorid: {author[0]}, authorname: {author[1]}, biography: {author[2]}\n")

    
   
    def update_books(self):
        bookid = self.bookid_entry.get()
        title = self.title_entry.get()
        authorid = self.author_id_entry.get()
        genreid = self.genre_id_entry.get()
        publisherid= self.publisher_id_entry.get()
        year=self.year_entry.get()

        if bookid == "" or title == "" or authorid == "" or genreid == "" or publisherid == "" or year=="":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("UPDATE Books SET title=?, authorid=?, genreid=?,publisherid=?,year=? WHERE bookid=?",
                            (title,authorid,genreid,publisherid,year,bookid))
        self.conn.commit()
        self.display_books()
        messagebox.showinfo("Success", "Books updated successfully")

    def update_authors(self):
        authorid = self.authorid_entry.get()
        authorname = self.authorname_entry.get()
        biography = self.biography_entry.get()
       

        if authorid == "" or authorname == "" or biography == "" :
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.cursor.execute("UPDATE Authors SET authorname=?, biography=? WHERE authorid=?",
                            (authorname,biography,authorid))
        self.conn.commit()
        self.display_authors()
        messagebox.showinfo("Success", "Author updated successfully")

    def delete_books(self):
        bookid = self.bookid_entry.get()
        if bookid== "":
            messagebox.showerror("Error", "Please enter Book id")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this Book?")
        if confirm:
            self.cursor.execute("DELETE FROM Books WHERE bookid=?", (bookid,))
            self.conn.commit()
            self.display_books()
            messagebox.showinfo("Success", "Books deleted successfully")

    def delete_authors(self):
        authorid = self.authorid_entry.get()
        if authorid == "":
            messagebox.showerror("Error", "Please enter Authorid")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this author?")
        if confirm:
            self.cursor.execute("DELETE FROM Authors WHERE authorid=?", (authorid,))
            self.conn.commit()
            self.display_authors()
            messagebox.showinfo("Success", "author deleted successfully")


root = tk.Tk()
app = BookManagementSystem(root)
root.mainloop()
