from sqlalchemy import Column , Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

#Declare the special class: Base that will be used to build tables mapping them to SQL tables
Base = declarative_base()

#Post Model 
class User(Base):
     __tablename__ ="Users"
     
     #Model Attributes
     User_ID = Column(Integer, primary_key=True)
     Username = Column(String, nullable = False , unique = True)
     Email = Column(String, nullable = False , unique = True)
     Password_Hashed = Column(String , nullable = False )  
     role = Column(String, nullable = False , default = 'user')
     Created_At = Column(DateTime, default=datetime.now)   
     
     #Specifying the relationship a user has to a post and that is one of an author and without a user a post cannot exist
     posts = relationship("Post", back_populates="author" , cascade = "all, delete-orphan")

class Post(Base):
     __tablename__="Posts"
     
     #Model Attributes
     Post_ID = Column(Integer, primary_key= True)
     User_ID = Column(Integer , ForeignKey = "Users.User_ID", nullable = False)
     Title = Column(String, nullable= False)
     Content = Column(String , nullable=False)
     Created_At = Column(DateTime, default=datetime.now) 
     Updated_At = Column(DateTime, default=datetime.now) 
     
     #Specifying the relationship a user has to a post and that is one of an author and without a user a post cannot exist
     author = relationship("User", back_populates="posts")