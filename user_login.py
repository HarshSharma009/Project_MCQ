import sqlite3
from getpass import getpass
import super_user
import student
conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute('create table user(username text,password text)')
#c.execute('create table details(name text,topic text,marks int,date text)')
#c.execute('create table questions(question text,a text,b text,c text,d text,correct text,topic text)')
#c.execute("insert into user values ('%s','%s')"%('admin','admin'))
#conn.commit()
n = input('Enter the choice(a/b):\n a->User\n b->student\n')
if n == 'a':
    while True:
        user = input('Enter the username: ')
        password = getpass('Enter the password: ')
        c.execute("select * from user where username = '%s'" % user)
        temp = c.fetchone()
        if temp is None:
            print('Invalid username')
        elif temp[1] == password:
            super_user.main()
            break
        else:
            print('Wrong password')
    conn.close()
else:
    conn.close()
    print('For Students'.center(32, '*'))
    student.main()
