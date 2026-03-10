from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import Session
from functions import post_list_all,add_post,find_post_by_id, post_list_per_user, del_post
from schemas import ReturnPost,ReturnPosts,CreatePost
from db import get_db



#instantiation of the users router 
router = APIRouter(prefix="/posts",tags= ["Posts"])

#Route for creating a new post
@router.post("/", response_model=ReturnPost)
#Endpoint to create a post
def post_creation(post : CreatePost, db: Session = Depends(get_db)):
    
    new_post =add_post(db,user_id=post.User_ID,title=post.Title,content=post.Content)
    return new_post

# Route to list all posts
@router.get("/", response_model=list[ReturnPosts])
#Endpoint for listing all posts in the db
def list_posts(db: Session = Depends(get_db)):
    return post_list_all(db)

#Route for listing a post by user id within the database
@router.get("/{post_id}", response_model=ReturnPost)
#Endpoint for returning a list of users
def get_post_by_id(post_id: int,user_id = int , db : Session = Depends(get_db)):
    post = find_post_by_id(db,user_id,post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post is not found")
    return post

#Route to delete a post from database based on their user id
@router.delete("/{post_id}")
#Endpoint for a post
def delete_post(post_id : int ,user_id: int,db: Session = Depends(get_db)):
    
    deleted_post = del_post(db,post_id,user_id)
    if not deleted_post :
        raise HTTPException(status_code=404,detail="Post is not deleted")
    return{"message":"Post successfully deleted from the database"}

# #Route to update a post's content
# @router.post("/{post_id}",response_model= schemas.pos)