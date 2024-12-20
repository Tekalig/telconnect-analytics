import os
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection parameters from the environment
DB_USERNAME = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Create the SQLAlchemy connection URL
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def get_db_connection():
    """Returns a connection to the PostgreSQL database."""
    try:
        connection = engine.connect()
        print("Database connection successful.")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def insert_data_from_dataframe(df, table_name="xdr_data"):
    """Insert data from a pandas DataFrame into the specified PostgreSQL table."""
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    try:
        # Insert data from DataFrame to PostgreSQL table
        with engine.connect() as connection:
            for index, row in df.iterrows():
                # Create a dictionary from the row (column name -> value)
                data = {col: row[col] for col in df.columns}

                # Insert the row into the table
                connection.execute(table.insert().values(data))
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")


def bulk_insert_data_from_dataframe(df, table_name="xdr_data"):
    """Insert data from a pandas DataFrame into the PostgreSQL table using bulk insert."""
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    try:
        # Convert the DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')

        # Insert all records in one go (bulk insert)
        with engine.connect() as connection:
            connection.execute(table.insert(), data)
        print("Bulk data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")


def retrieve_data_from_database(table_name="xdr_data"):
    """Retrieve data from the specified PostgreSQL table."""
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    try:
        # Query the table
        with engine.connect() as connection:
            result = connection.execute(table.select()).fetchall()

        # Convert the result to a pandas DataFrame
        df = pd.DataFrame(result, columns=table.columns.keys())
        return df
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None
