from app.db import get_db
from app.crud import create_user, get_users, create_price, get_prices

def main():
    db = next(get_db())

    # Create a new user
    user = create_user(db, name="John Doe", age=30)
    print(f"User created: {user.name}, age {user.age}")

    #create_price(db, timestamp=1234567890, price=1234.56)

    # Get all users
    users = get_users(db)
    print("All users:", users)

    # Get all prices
    prices = get_prices(db)
    print("All prices:", prices)

if __name__ == "__main__":
    main()
