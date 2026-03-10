from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import Session
from program_security import verify_password, create_access_token
from functions import find_user_by_email
from schemas import LoginSchema,Token
from  db import get_db

router = APIRouter(
    prefix= "/login",
    tags=["login"]
)

#Route for user login
@router.post("/login",response_class=Token)
def login(credentials : LoginSchema, db: Session=Depends(get_db)):
    user = find_user_by_email(db,credentials.Email)
    
    if not user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    if not verify_password(credentials.Password,user.Password_Hash):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    jwt_token = create_access_token(
        data={"user_id": user.User_ID}
    )
    
    return{
        "access_token": jwt_token,
        "token_type": "bearer"
        
    }
    