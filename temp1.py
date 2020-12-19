import sqlite3
conn = sqlite3.connect('sample.db')
c = conn.cursor()
c.execute("select * from students")
print(c.fetchall())
conn.close()