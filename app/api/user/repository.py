from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.api.user import model, schema


def get_user_by_username(db: Session, username):
    user = db.query(model.User).filter(
        model.User.username == username).one_or_none()

    if user is None:
        return None

    return user.to_Json()


def create_user(db: Session, user: schema.CreateUser):
    user_exist = get_user_by_username(db=db, username=user.username)
    if user_exist is None:
        db_user = model.User(
            username=user.username,
            user_password=user.user_password,
            user_email=user.user_email,
            user_firstname=user.user_firstname,
            user_lastname=user.user_lastname)
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        except Exception as ex:
            raise ex
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='User {} already exist'.format(user.username))
    return db_user.to_Json()


def fetch_all(db: Session):
    try:
        users = db.query(model.User).all()
    except Exception as ex:
        raise ex
    return users


def update_user(db: Session, username, user: schema.UpdateUser):
    db_user = db.query(model.User).filter(
        model.User.username == username).one_or_none()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user: {} not found".format(username))
    try:
        if db_user.user_password != user.user_password and user.user_password != '' or user.user_password is not None:
            db_user.user_password = user.user_password
        if db_user.user_email != user.user_email and user.user_email != '' or user.user_email is not None:
            db_user.user_email = user.user_email
        if db_user.user_firstname != user.user_firstname and user.user_firstname != '' or user.user_firstname is not None:
            db_user.user_firstname = user.user_firstname
        if db_user.user_lastname != user.user_lastname and user.user_lastname != '' or user.user_lastname is not None:
            db_user.user_lastname = user.user_lastname
        db.commit()
        db.refresh(db_user)
    except Exception as ex:
        raise ex
    return db_user
