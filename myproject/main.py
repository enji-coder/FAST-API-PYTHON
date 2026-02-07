from fastapi import FastAPI

from student import student_router

#creating instance of FastApi() 
app = FastAPI() 

@app.get("/")
def home():
    return {"message":"this is main route"}


#including  routers 
app.include_router(student_router)
