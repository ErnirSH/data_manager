from sqlalchemy.orm import Session
from .models import User, BitcoinPrice

# Create a new user
def create_user(db: Session, name: str, age: int):
    new_user = User(name=name, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
def get_users(db: Session):
    return db.query(User).all()

# Get a user by ID
def get_user(db: Session, user_id):
    return db.query(User).filter(User.id == user_id).first()

# Update a user
def update_user(db: Session, user_id, name: str = None, age: int = None):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if name:
            user.name = name
        if age:
            user.age = age
        db.commit()
        db.refresh(user)
    return user

# Delete a user
def delete_user(db: Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def create_price(db: Session, timestamp: int, price: float):
    new_price = BitcoinPrice(timestamp=timestamp, price=price)
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    return new_price

def get_prices(db: Session):
    return db.query(BitcoinPrice).all()
