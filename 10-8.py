import sqlite3 as lite
con = lite.connect('mtica.db')


cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS CARS")
cur.execute('''CREATE TABLE Cars(
        Id INT,Name TEXT,Price INT)''')
print("TABLES CARS CREATED")
cur.execute("INSERT INTO Cars VALUES(1,'AUDI',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'MERCEDES',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'volvo',5262)")
cur.execute("INSERT INTO Cars VALUES(5,'bently',52142)")
cur.execute("INSERT INTO Cars VALUES(6,'citroen',677642)")
cur.execute("INSERT INTO Cars VALUES(7,'hummer',57642)")
cur.execute("INSERT INTO Cars VALUES(8,'volkswagen',52772)")

con.commit()
print("values in table car inserted.")
