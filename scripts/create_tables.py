from app.db import engine, Base
# noinspection PyUnresolvedReferences
from app.models import User, BitcoinPrice

# Create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
