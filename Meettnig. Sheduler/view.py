#view
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import model


class MeetingScheduler(model.Model):
    def __init__(self, root):
        self.root = root
        self.root.title("Meeting Scheduler")
        self.root.geometry("900x700")

        self.q = tk.StringVar()
        self.t1 = tk.StringVar()
        self.t2 = tk.StringVar()
        self.t3 = tk.StringVar()
        self.t4 = tk.StringVar()
        self.t5 = tk.StringVar()
        self.t6 = tk.StringVar()
        self.t7 = tk.StringVar()

        self.wrapper1 = ttk.LabelFrame(root, text="Scheduled Meetings")
        self.wrapper2 = ttk.LabelFrame(root, text="Search")
        self.wrapper3 = ttk.LabelFrame(root, text="Meeting Details")

        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        self.trv = ttk.Treeview(self.wrapper1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="6")
        self.trv.pack()

        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="Title")
        self.trv.heading(3, text="Date (YYYY-MM-DD)")
        self.trv.heading(4, text="Time (HH:MM:SS)")
        self.trv.heading(5, text="Link")
        self.trv.heading(6, text="Location")
        self.trv.heading(7, text="Description")

        self.trv.bind('<Double 1>', self.get_row)

        self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="rootroot", database="sys", auth_plugin="mysql_native_password")
        self.cursor = self.mydb.cursor()

        # Create widgets for search and user data input
        self.create_search_widgets()
        self.create_user_data_widgets()

    def create_search_widgets(self):
        lbl = ttk.Label(self.wrapper2, text="Search")
        lbl.pack(side=tk.LEFT, padx=10)
        end = ttk.Entry(self.wrapper2, textvariable=self.q)
        end.pack(side=tk.LEFT, padx=6)
        btn = ttk.Button(self.wrapper2, text="Search", command=self.search)
        btn.pack(side=tk.LEFT, padx=6)
        cbtn = ttk.Button(self.wrapper2, text="Clear", command=self.clear)
        cbtn.pack(side=tk.LEFT, padx=6)

    def create_user_data_widgets(self):
        labels = ["ID", "Title", "Date", "Time", "Link", "Location", "Description"]
        entries = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7]

        for i, label_text in enumerate(labels):
            label = ttk.Label(self.wrapper3, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=3)
            entry = ttk.Entry(self.wrapper3, textvariable=entries[i])
            entry.grid(row=i, column=1, padx=5, pady=3)

        up_btn = ttk.Button(self.wrapper3, text="Update", command=self.update_db)
        add_btn = ttk.Button(self.wrapper3, text="Add New", command=self.add_db)
        delete_btn = ttk.Button(self.wrapper3, text="Delete", command=self.delete_db)

        up_btn.grid(row=7, column=0, padx=5, pady=3)
        add_btn.grid(row=7, column=1, padx=5, pady=3)
        delete_btn.grid(row=7, column=2, padx=5, pady=3)

    def update(self, rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i)



    def get_row(self, event):
        row_id = self.trv.identify_row(event.y)
        item = self.trv.item(self.trv.focus())
        self.t1.set(item['values'][0])
        self.t2.set(item['values'][1])
        self.t3.set(item['values'][2])
        self.t4.set(item['values'][3])
        self.t5.set(item['values'][4])
        self.t6.set(item['values'][5])
        self.t7.set(item['values'][6])


