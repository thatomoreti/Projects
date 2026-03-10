from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import Session
from functions import user_list_all,add_user,find_user_by_id,del_user
from schemas import ReturnUser,ReturnUsers,CreateUser
from  db import get_db

#instantiation of the users router 
router = APIRouter(prefix= "/users",tags= ["Users"])

#Route for creating a new users 
@router.post("/",response_model=ReturnUser)
#Endpoint for creating a user , validates json request using CreateUser schema and the db session is injected va Dependency Injection
def user_creation(user: CreateUser, db: Session = Depends(get_db)):
    try:
        new_user = add_user(db,
                                    username=user.Username,
                                    email= user.Email,
                                    password_hashed=user.Password_Hash)
        return new_user
    except ValueError as error:
        #If there's a duplicate email
        raise HTTPException(status_code=400,detail=str(error))

# Route to list all users
@router.get("/", response_model=list[ReturnUser])
#Endpoint for listing all users in the db
def list_users(db: Session = Depends(get_db)):
    return user_list_all(db)

#Route for listing a user by user id within the database
@router.get("/{user_id}", response_model=ReturnUser)
#Endpoint for returning a list of users
def get_user_by_id(user_id = int , db : Session = Depends(get_db)):
    user = find_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user

#Route to delete a user from database based on their user id
@router.delete("/{user_id}")
#Endpoint for deleting a user
def delete_user(user_id: int,db: Session = Depends(get_db)):
    
    deleted_user = del_user(db,user_id)
    if not deleted_user :
        raise HTTPException(status_code=404,detail="User not deleted")
    return{"message":"User successfully deleted from the database"}