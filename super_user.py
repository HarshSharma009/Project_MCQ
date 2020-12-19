import sqlite3



def add_question():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    topic = input("Enter the topic name: ")
    ques = input("Enter the question: ")
    opa = input("Enter option a: ")
    opb = input("Enter option b: ")
    opc = input("Enter option c: ")
    opd = input("Enter option d: ")
    correct = input("Correct option: ")
    c.execute("insert into questions values('%s','%s','%s','%s','%s','%s','%s')" % (
        ques, opa, opb, opc, opd, correct, topic))
    conn.commit()
    conn.close()


def print_student_marks():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("select * from details")
    print('MARKS:\nName\t\tTopic\t\tMarks\t\tDate')
    for i in c.fetchall():
        print(i[0], i[1], i[2], i[3], sep='\t\t')
    conn.close()


def main():
    n = ''
    while n != 'q':
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        print('Enter the choice')
        print('1:Add user\n2:Add Question\n3:View student Marks\nq:quit')
        n = input()
        if n == '1':
            c.execute("insert into user values('%s','%s')" %
                      (input('Enter new username: '), input('Enter password: ')))
            conn.commit()
            conn.close()
        elif n == '2':
            add_question()
            conn.close()
        elif n == '3':
            print_student_marks()
            conn.close()
