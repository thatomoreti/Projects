from passlib.context import CryptContext #Importing a password security manager that knows how to hash passwords
from jose import JWTError,jwt #Importing jwt package to encode and decode the jwt token
from datetime import datetime,timedelta #Importing datetime package to set token expiration time and get current time 
from dotenv import load_dotenv #Importing dotenv library to have access to the env variables
import os  #Importing the operating system of the computer to allow me to be able to read the env file

load_dotenv() #Loads env variables

#Reading the env files and storing the environment variable values to variables
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY=os.getenv("SECRET_KEY")

#Declare Cryptcontext obj
password_context  = CryptContext(
    #Choosing which hashing method to use
    schemes=["bycrypt"],
    
    #Setting for the auto marking of old hashes as deprecated
    deprecated ="auto"
)
#function meant to hash passwords 
def password_hash(password : str)-> str:
    #returns a hashed version of a password
    return password_context.hash(password)

#Function to check if password was hashed properly 
def verify_password(normal_password: str, hashed_password : str)-> bool:
    return password_context.verify(normal_password,hashed_password)

#Function to create jwt token by encoding data and setting expiration of tokens
def create_access_token(data:dict):
    #Make copy of data to avoid changing actual data
    data_to_encode = data.copy()
    
    #Token expiration time
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({"exp":expiration})
    
    #Encode payload 
    encoded_jwt = jwt.encode(data_to_encode,SECRET_KEY, algorithm=ALGORITHM)
    
    #Return jwt access token
    return encoded_jwt
