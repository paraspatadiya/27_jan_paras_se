import sqlite3
try:
    con=sqlite3.connect("mydb")
    print("database created and connected successfully")
except Exception as e:
    print(e)
create="create table emp(id integer primary key autoincrement,name text,empid text)"
try:
    con.execute(create)
    print("Table Created!")
except Exception as e:
    print(e)
insert="insert into emp(name,empid)values('paras','raj 81'),('uday','raj 200'),('hitesh','raj 301')"
try:
    con.execute(insert)
    con.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)
update="update emp set name='darshan' where empid=301"
try:
    con.execute(update)
    con.commit()
    print("Record Updated!")
except Exception as e:
    print(e)
dlt="delete from emp where empid=81"
try:
    con.execute(dlt)
    con.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)
