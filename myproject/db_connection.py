import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student
               (id integer primary key autoincrement,
               name text,
               subject text,
               city text)
""")
conn.commit()
# cursor.execute("delete from Student")
# cursor.execute("""
#                insert into Student (name,subject,city)
#                values 
#                ('Anjali',"python","Ahmedabad"),
#                ('Priya',"Java","Mumbai"),
#                ('Shreya',"Data science","Delhi")
#                """)


cursor.execute("select * from Student")
records = cursor.fetchall()

for row in records:
    print(f"{row[0]}  {row[1]}  {row[2]}")

conn.commit()




