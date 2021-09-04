import sqlite3
from guizero import *
# DB_MAKER IS MOSTLY DONE, IF I COULD ONLY GET IT TO GIVE ME THE SERIAL NUMBER THE 
# THE WAY I WANT IT THAT WOULD BE GREAT

class db_maker:
    def __init__(self):
        self = self

    def mood_db_setUp(self):
        f = 0 
        self.conn = sqlite3.connect("mood_tracker.db")

        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS moodToday ('id' INTEGER, 'moodToday' INTEGER, 'moodTomorrow' INTEGER, 'hygiene' INTEGER, 'spirituality' INTEGER, 'healthEating' INTEGER, 'noGoToWork' INTEGER, 'noworkOut' INTEGER, 'addiction' INTEGER, 'total' INTEGER, 'notes' TEXT); """)

        self.conn.commit()

        f = 1
        while f != 1:
            self.conn.close() # I STILL NEED TO FIGURE OUT HOW TO OPEN AND CLOSE THE DB 

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

    #THIS METHOD ATTEMPTS TO TAKE THE ID VALUE AND ADD ONE TO BE ABLE TO CREATE A SERIALIZED CONTROL SYSTEM
    #I WAS ABLE TO FIGURE OUT HOW TO TO GET IT TO PRINT THE VALUE QUERIED BUT THAT IS ABOUT IT. 
    # WHAT I WANT IS TO BE ABLE TO A RANDOM STARTING VALUE AND ADD 1 FROM THERE BUT I THINK A TOTALLY RANDOM 
    # SERIAL NUMBER WILL BE THE BEST I CAN DO. 
    def db_id_Selector(self, id_one):
        f = 0
        self.cur = self.conn.cursor()
        self.cur.execute("""SELECT id FROM moodToday ORDER BY id DESC LIMIT 1;""")
        last_val = self.cur.fetchone()
        if id_one != None:
            last_val += 1
        
        id_one = last_val
        f = 1

"""IN ANOTHER CLASS PERHAPS, ENVISION IN MY APP A SMALL NOTEPAD TO BE ABLE 
    TO WRITE SOME SENTIMENTS DOWN. MAYBE AN OVERLAYER APP THAT SERVES AS THE GUI LOGIN"""

class second_App:

    def __init__(self):
        self = self

    def second_Wind_app(self):
        self.second = App(title="Database Entry Display", width=780, height=1000, layout="grid")
    
        
        
        self.second.display()