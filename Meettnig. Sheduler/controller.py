#controller

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import model
import view

class Meeting(view.MeetingScheduler):
    pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Meeting(root)
    root.mainloop()