from fastapi import APIRouter

student_router = APIRouter(
    prefix="/student",
    tags=["students"]  # swagger group 
)

@student_router.get("/")
def display():
    return {"message":"student display"}


