from sqlalchemy import create_engine #library to connect python with mssql
from dotenv import load_dotenv  # library to allow the use of env file
import os  #Importing the operating system of the computer to allow me to be able to read the env file

load_dotenv() #Loads env variables

#Reading the env files and storing the environment variable values to variables
DB_SERVER=os.getenv("DB_SERVER")
DB_NAME=os.getenv("DB_NAME")
DB_DRIVER=os.getenv("DB_DRIVER")
DB_USER= os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")

#Creating connection to DB
DB_URL = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}&trusted_connection=yes"

#Facilitate the connection(DB_URL) of the DB to python safely
engine = create_engine(DB_URL)

#Testing the created connection to the db
with engine.connect() as connection:
    print("DB connected!")