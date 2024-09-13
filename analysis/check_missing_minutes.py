from app.db import get_db  # Reuse your DB connection logic
from datetime import datetime, timedelta, timezone
from app.models import BTC2020Min  # Assuming the model is defined as above

def check_missing_minutes():
    db = next(get_db())  # Get a DB session

    try:
        # Query all entries ordered by unix timestamp
        entries = db.query(BTC2020Min).order_by(BTC2020Min.unix).all()

        missing_minutes = []
        prev_timestamp = None
        prev_vol = None
        prev_date = None

        for entry in entries:
            if entry.volume_usd == '0.0' and prev_vol == '0.0':
                print(entry.date, entry.volume_usd)
                print(prev_date, prev_vol)
                print('-------------------------')
            if prev_vol == 0 and entry.volume_usd == 0:
                print(entry.date)

            current_timestamp = datetime.fromtimestamp(entry.unix, tz=timezone.utc)
            if prev_timestamp:
                # Calculate the time difference between the current and previous timestamp
                diff = current_timestamp - prev_timestamp
                if diff.total_seconds() > 60:
                    missing_minutes.append((prev_timestamp, current_timestamp, diff))
            prev_vol = entry.volume_usd
            prev_date = entry.date
            prev_timestamp = current_timestamp

        if missing_minutes:
            print(f"Found {len(missing_minutes)} instances where minutes are missing:")
            for prev, current, diff in missing_minutes:
                print(f"Missing from {prev} to {current} (Difference: {diff})")
        else:
            print("No missing minutes found.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    check_missing_minutes()
