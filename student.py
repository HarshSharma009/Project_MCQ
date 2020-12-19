import sqlite3
from datetime import datetime


def run_quiz(name):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    marks = 0
    c.execute("select distinct(topic) from questions")
    print('Available topics are: ')
    for i in c.fetchall():
        print(i[0], end='\t')
    print()
    topic = input("Enter the topic: ")
    c.execute("select * from questions where topic='%s'" % (topic))
    temp = c.fetchall()
    conn.commit()
    conn.close()
    if len(temp)==0:
        print('Invalid topic selected')
        
    else:
            
        
        for i in temp:
            print(i[0])
            print('a:', i[1], '\tb:', i[2], '\tc:', i[3], '\td:', i[4])
            ans = input("answer: ")
            if ans == i[5]:
                marks += 1
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("insert into details values ('%s','%s','%d','%s')" %
                  (name, topic, marks, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        print("You obtained %d marks" % marks)


def main():
    name = input('Enter your name: ')
    run_quiz(name)
