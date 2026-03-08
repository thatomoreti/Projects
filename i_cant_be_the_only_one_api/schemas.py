from pydantic import BaseModel, EmailStr # importing basemodel as the main schema class most of the schemas are going to inherit from and the EmailStr class is for email validation 
from typing import Optional, List # Optional class is to make it so that a field can be optional
from datetime import datetime # For timestamps 


#Schema for user creation(Request)
class CreateUser(BaseModel):
    #Schema validates all data INPUTS necessary for creating a user
    Username : str
    Email : EmailStr
    Password_Hash : str
    
    # #To map the schema to the python model, orm mode needs to be set to true
    # class Config:
    #     orm_mode = True   
#Schema that returns a user to the client(Response) w/o password for safe API practice
class ReturnUser(BaseModel):
    #Schema stipulates the data that needs to be returned to the client by giving them only what they would need to know 
    User_ID : int
    Username : str
    Email : EmailStr
    role : str
    Created_At : datetime
    
    #To map the schema to the python model, orm mode needs to be set to true
    class Config:
        orm_mode = True
        
        
#Schema for returning a list of users 
class ReturnUsers(BaseModel):
    users : List[ReturnUser] 


#Schema for the creation of posts
class CreatePost(BaseModel):
    #Schema validates all post data inputs needed for creating a post
    Title : str
    Content : str
    
#Schema to return the post that has been just created 
class ReturnPost(BaseModel):
    #Schema is selective of which functions are relevant to the client
    Post_ID : str
    User_ID : str
    Title:str
    Content : str
    Created_At : datetime
    Update_At : Optional[datetime] =None
    
    class Config():
        orm_mode = True
        
#Schema returning a list of posts
class ReturnPosts(BaseModel):
    posts : List[ReturnPost]