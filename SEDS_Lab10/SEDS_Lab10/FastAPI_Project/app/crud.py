from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_user_posts(db: Session,user_id: int ,skip: int = 0, limit: int = 100):
    query =  db.query(models.Post).filter(models.Post.author == user_id).offset(skip).limit(limit)
    return query.all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email,name=user.name)
    # instance object added to database session
    db.add(db_user)
    # changes are saved to the database
    db.commit()
    # instance is refreshed to contain any new data from the database, like the generated ID
    db.refresh(db_user)
    return db_user

def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    # If no publishedAt is provided, set it to the current time
    if not post.publishedAt:
        post.publishedAt = datetime.utcnow()  # Use UTC time or local time as needed

    db_post = models.Post(**post.dict(), author=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_user_post(db: Session,post: schemas.Post):
    db.delete(post)
    db.commit()