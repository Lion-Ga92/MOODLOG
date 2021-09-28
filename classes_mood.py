import sqlite3
from tkinter import Button, Message
from guizero import *
from guizero import PushButton
# DB_MAKER IS DONE, I JUST NEED TO REFACTOR IT TO GET A CLEANER CODE


class db_maker:
    def __init__(self):
        self = self

    def mood_db_setUp(self):
        f = 0 
        self.conn = sqlite3.connect("mood_tracker.db")

        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS moodToday ('date' TEXT, 'moodToday' INTEGER, 'moodTomorrow' INTEGER, 'hygiene' INTEGER, 'spirituality' INTEGER, 'healthEating' INTEGER, 'noGoToWork' INTEGER, 'noworkOut' INTEGER, 'addiction' INTEGER, 'total' INTEGER, 'notes' TEXT); """)

        self.conn.commit()

        f = 1
        while f != 1:
            self.conn.close() # I STILL NEED TO FIGURE OUT HOW TO OPEN AND CLOSE THE DB AS I DONT THINK THIS IS ACCURATE OR FUNCTIONAL 

    def db_adder(self, a, b, c, d, e, g, h, i, j, k, m):
        f = 0
        self.a = a
        self.b = b 
        self.c = c
        self.d = d
        self.e = e 
        self.g = g 
        self.h = h
        self.i = i
        self.j = j 
        self.k = k
        self.m = m

        list_o__vals = [self.a, self.b, self.c, self.d, self.e, self.g, self.h, self.i, self.j, self.k, self.m]

        self.cur = self.conn.cursor()
        self.cur.execute("""INSERT INTO moodToday VALUES (?,?,?,?,?,?,?,?,?,?,?); """, list_o__vals)

        self.conn.commit()
        f = 1

    # THIS METHOD ATTEMPTS TO TAKE A USER SELECTED VALUE AND RETURN TO THE CONSOLE THE ROW DATA 
    # REQUESTED IN THE MAIN FILE. THE TROUBLE IS THAT I EITHER GET AN OUTPUT OF NONE FOR THE DATA 
    # OR RUN INTO A SQLITE OPERATIONAL ERROR 'ROW VALUE MISUSED'
    def db_id_Selector(self, val):
        f = 0
        self.val = val
        self.cur = self.conn.cursor()
        self.cur.execute("""SELECT * FROM moodToday WHERE date = (?, ?, ?, ?, ?, ?, ?, ?, ?);""", self.val)
        print(self.cur.fetchall())
        f = 1
