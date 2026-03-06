from models import User,Post
from sqlalchemy.orm import Session

#Function that finds a user based on their email
def find_user_by_email(db: Session,email: str):
    return db.query(User).filter(User.Email == email).first()

#Function that finds a user based on their user id
def find_user_by_id(db: Session,user_id: int):
    return db.query(User).filter(User.User_ID == user_id).first()

#Function to list all user for potential admin functionality
def user_list_all(db: Session):
    return db.query(User).all()

#Function that creates a user within the database
def add_user(db:Session,username:str,email:str,password_hashed:str,role: str="user"):
    #Check for duplicate users/email
    user = find_user_by_email(db,email)
    if user :
        raise ValueError("The email is already registered.")
    new_user = User(Username = username,Email = email,Password_Hash = password_hashed,role = role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Function that deletes a user for potential admin functionality
def del_user(db: Session, user_id: int):
    
    existing_user= find_user_by_id(db,user_id)
    
    if existing_user:
        db.delete(existing_user)
        db.commit()
        return True
    return False

#Function that creates a post for a user within the database
def add_post(db:Session,user_id: int,title:str,content:str):
    
    #Check if user exists
    existing_user= find_user_by_id(db,user_id)
    if not existing_user :
        raise ValueError("This user does not exist .")
    new_post = Post(User_ID = user_id,Title = title,Content = content)
    db.add(new_post)
    db.commit()   
    db.refresh(new_post)
    return new_post

#Function that finds a post based on its id and user
def find_post_by_id(db: Session,user_id: int,post_id: int):
    return db.query(Post).filter(Post.Post_ID == post_id,Post.User_ID == user_id).first()

#Function that deletes a post , only to be done by the user
def del_post(db: Session, post_id: int, user_id : int):
    existing_post= find_post_by_id(db,user_id,post_id)
    if existing_post:
        db.delete(existing_post)
        db.commit()
        return True
    return False

#Function that allows the user to update their post 
def update_post(db: Session, post_id : int, user_id: int,content:str):
    existing_post = find_post_by_id(db,user_id,post_id)
    if existing_post:
        existing_post.Content= content
        db.commit()
        db.refresh(existing_post)
        return existing_post
    return None

#Function to list posts for a single user
def post_list_per_user(db: Session,user_id: int):
    return db.query(Post).filter(Post.User_ID == user_id).all()

#Function to list all posts for the feed
def post_list_all(db: Session):
    return db.query(Post).order_by(Post.Created_At.desc()).all()
