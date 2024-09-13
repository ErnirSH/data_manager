import requests
from app.db import get_db  # Reuse database session management
from app.models import BitcoinPrice

# CoinGecko API URL for hourly data over the past year
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90&x_cg_demo_api_key=CG-aPXtLzcsjMJF2GiVd2EMgYAU'

# Fetch the data from CoinGecko
response = requests.get(url)
data = response.json()

# Extract the prices (timestamp and price)
prices = data['prices']  # List of [timestamp, price]

def populate_bitcoin_data():
    db = next(get_db())  # Get the database session from db.py

    try:
        # Fetch all existing timestamps in a single query
        existing_timestamps = set(
            row.timestamp for row in db.query(BitcoinPrice.timestamp).all()
        )

        # Prepare a list to hold new BitcoinPrice objects for bulk insert
        new_prices = []

        for price_data in prices:  # Assuming 'prices' is a list of (timestamp, price)
            timestamp, price = price_data

            # Convert timestamp to seconds and check if it already exists
            if (timestamp // 1000) not in existing_timestamps:
                new_price = BitcoinPrice(timestamp=timestamp // 1000, price=price)
                new_prices.append(new_price)

        # Bulk insert the new records
        if new_prices:
            db.bulk_save_objects(new_prices)
            db.commit()
            print(f"Inserted {len(new_prices)} new prices into the database.")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Roll back any changes in case of error

# def populate_bitcoin_data():
#     db = next(get_db())  # Get the database session from db.py
#
#     try:
#         for price_data in prices:
#             timestamp, price = price_data
#             existing_entry = db.query(BitcoinPrice).filter(BitcoinPrice.timestamp == timestamp).first()
#
#             if not existing_entry:
#                 new_price = BitcoinPrice(timestamp=timestamp // 1000, price=price)  # Convert ms to seconds
#                 db.add(new_price)
#
#         db.commit()
#         print("Bitcoin price data has been successfully inserted into the database.")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         db.rollback()  # Roll back any changes in case of error

if __name__ == "__main__":
    populate_bitcoin_data()
