"""
from fastapi import FastAPI
import sqlite3
import os 
# create an instance of app 
app = FastAPI() 

@app.get("/")
def greetings():
    return {"message" : "hello welcome to fastapi"}

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(BASE_DIR, "student.db")

# for database connection 
def get_db_connection():    
    conn = sqlite3.connect("../student.db")
    conn.row_factory = sqlite3.Row  # allows dict-like access
    return conn


# now, fetch all records from student 
@app.get("/students")
def get_all_student():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("select * from Student")
    students = cursor.fetchall()

    conn.close() 

    # convert rows to list of dict 

    result = [] 
    for stu in students:
        result.append({
            "id" : stu["id"],
            "name" : stu["name"],
            "subject" : stu["subject"],
            "city" : stu["city"]
        })
    return result


"""