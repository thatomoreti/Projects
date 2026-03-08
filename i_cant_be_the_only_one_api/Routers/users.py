from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import Session
from .. import functions
from .. import schemas
from .. db import get_db

#instantiation of the users router 
router = APIRouter(prefix= "/users",tags= ["Users"])

#Route/Endpoint for creating a new users 
@router.post("/",response_model=schemas.ReturnUser)
#function for creating a user , validates json request using CreateUser schema and the db session is injected va Dependency Injection
def user_creation(user: schemas.CreateUser, db: Session = Depends(get_db)):
    try:
        new_user = functions.add_user(db,
                                    username=user.Username,
                                    email= user.Email,
                                    password_hashed=user.Password_Hash)
        return new_user
    except ValueError as error:
        #If there's a duplicate email
        raise HTTPException(status_code=400,detail=str(error))

# Route/Endpoints to list all users
@router.get("/", response_model=list[schemas.ReturnUser])
def list_users(db: Session = Depends(get_db)):
    return functions.user_list_all(db)

#Route/Endpoint for listing a user by user id within the database
@router.get("/{user_id}", response_model=schemas.ReturnUser)
#Function for returning a list of users
def get_user_by_id(user_id = int , db : Session = Depends(get_db)):
    user = functions.find_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user

