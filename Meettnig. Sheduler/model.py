#model
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Model:

    def search(self):
        q2 = self.q.get()
        query = f"Select id,title,dat,tim,link,location,des from meet where id like '%{q2}%' OR title like '%{q2}%' OR dat like '%{q2}%' OR tim like '%{q2}%' OR link like '%{q2}%' OR des like '%{q2}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.update(rows)

    def clear(self):
        query = "Select id,title,dat,tim,link,location,des from meet"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.update(rows)

    def update_db(self):
        id = self.t1.get()
        title = self.t2.get()
        dat = self.t3.get()
        tim = self.t4.get()
        link = self.t5.get()
        loc = self.t6.get()
        des = self.t7.get()

        if messagebox.askyesno("Confirm?"):
            query = "Update meet set id = %s, title = %s , dat = %s, tim= %s , link=%s, location = %s, des=%s where id = %s"
            self.cursor.execute(query, (id, title, dat, tim, link, loc, des, id))
            self.mydb.commit()
            self.clear()

    def add_db(self):
        id = self.t1.get()
        title = self.t2.get()
        dat = self.t3.get()
        tim = self.t4.get()
        link = self.t5.get()
        loc = self.t6.get()
        des = self.t7.get()
        query = "Insert into meet values (%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(query, (id, title, dat, tim, link, loc, des))
        self.mydb.commit()
        self.clear()

    def delete_db(self):
        id = self.t1.get()
        if messagebox.askyesno("Confirm Deletion?"):
            query = f"Delete From meet where id = {id}"
            self.cursor.execute(query)
            self.mydb.commit()
            self.clear()
