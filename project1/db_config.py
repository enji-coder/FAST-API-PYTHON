
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# ==============================
# step : 1 Database Configuration
# ==============================

DATABASE_URL = "mysql+pymysql://root:123456789@localhost/fastapi_db1"

# ==============================
# step : 2 Creating Engine 
# ==============================

#engine creation 
engine = create_engine(DATABASE_URL,echo=True)  # echo Shows SQL queries in terminal

# ==============================
# step : 3  Create Session
# ===============================

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

# ==============================
# step : 4  Base class for model 
# ==============================
Base = declarative_base()

# ==============================
# step : 5 Dependency (For FastAPI)
# ==============================

def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()