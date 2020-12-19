import sqlite3
conn = sqlite3.connect('sample.db')
c = conn.cursor()
#c.execute('create table students(name text,rno int)')
c.execute("insert into students values('varaprasad',24)")
conn.commit()
conn.close()