#--> create_engine - it create a connection between python and mysql
from sqlalchemy import create_engine

#--> sessionmaker : this create database session 

"""
temporary conversation with database 
insert,update,read,.etc  without session we can't talk with database
"""

#--> declarative_base
"""
this is a base class that all your database models will inherit from it. 
"""
from sqlalchemy.orm import sessionmaker,declarative_base

