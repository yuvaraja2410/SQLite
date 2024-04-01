import sqlite3
from sqlite3 import Error
import os.path

def insertion(dbase):
    dbase.execute('''insert into demo values('Google','demo@gmail.com','12345678');''')
    dbase.execute('''insert into demo values('Microsoft','demo@gmail.com','12345678');''')
    dbase.commit()

def display(dbase):
    dis = dbase.execute('''select * from demo where username = 'demo@gmail.com';''')
    for i in dis:
        print(i[0]+"    "+str(i[1])+"   "+str(i[2]))
    print(" ") 
    dbase.commit()

def update(dbase):
     print("Before Execution \n")
     upd = dbase.execute('''select * from demo''')
     for i in upd:
        print(i[0]+"    "+str(i[1])+"   "+str(i[2])) 

     print("\nAfter Execution \n")
     upd = dbase.execute('''update demo set password = 'UpdatedPassword' where name = 'Google';''')
     dbase.commit()
     upd = dbase.execute('''select * from demo''')
     for i in upd:
        print(i[0]+"    "+str(i[1])+"   "+str(i[2])) 
     


def main():
        dbase = sqlite3.connect("demo.db")
        try:
            if os.path.exists("/home/geekster/Projects/Sqlite_Demo/demo.db"):
                dbase.execute('''create table demo(name text,username text,password text);''')                
        except:
                print("Connection success full\n")

        insertion(dbase)

        display(dbase)

        update(dbase)

if __name__ == "__main__":
    main()