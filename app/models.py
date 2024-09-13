from sqlalchemy import Column, Integer, String, Float
from .db import Base

# Define a simple User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age})>"

class BitcoinPrice(Base):
    __tablename__ = 'bitcoin_prices'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(Integer, unique=True, index=True)  # UNIX timestamp
    price = Column(Float)

    def __repr__(self):
        return f"<BitcoinPrice(id={self.id}, timestamp={self.timestamp}, price={self.price})>"


class BTC2020Min(Base):
    __tablename__ = 'btc_2020min'
    unix = Column(Integer, primary_key=True)  # Assuming 'unix' is unique
    date = Column(String)
    symbol = Column(String)
    open = Column(String)
    high = Column(String)
    low = Column(String)
    close = Column(String)
    volume_btc = Column('Volume BTC', String)  # Adjusting column name to match the table
    volume_usd = Column('Volume USD', String)  # Adjusting column name to match the table

    def __repr__(self):
        return f"<BTC2020Min(unix={self.unix}, date={self.date}, open={self.open}, high={self.high}, close={self.close})>"