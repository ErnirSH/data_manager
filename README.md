# My Project

This is a minimal project to demonstrate separation of concerns and SQLAlchemy database connections.

### Structure:
- `app/`: Contains database connection logic, models, and CRUD operations.
- `scripts/`: Contains scripts for creating tables or seeding data.
- `main.py`: Main entry point to the application for testing.

### Installation:

1. Clone the repository.
2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your database URL to the `.env` file.

5. Create the database tables:
    ```bash
    python scripts/create_tables.py
    ```

6. Run the main script:
    ```bash
    python main.py
    ```
