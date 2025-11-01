"""Set up the ALX_prodev MySQL database."""
import mysql.connector
from uuid import uuid4
from csv import DictReader


def connect_db():
    """Connect to the mysql database server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )
        print("Successfully connected to MySQL server.")
        return connection
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None

def create_database(connection):
    """Create the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("ALX_prodev database has been created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed to create database {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database in MYSQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="ALX_prodev" 
        )
        print("Successfully connected to ALX_prodev database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Failed to connect to ALX_prodev {err}")
        return None

def create_table(connection):
    """Create user_data table if it doesn't exist with the required fields."""
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor.execute(create_table_query)
        print("Successfully created user_data table.")
    except mysql.connector.Error as err:
        print(f"Failed to create user_data table.")
    finally:
        cursor.close()

def insert_data(connection, data):
    """Insert data in the database if it does not exist."""
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    with open("user_data.csv", newline='', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data_list = list(reader)
    for row in data_list:
        user_id = str(uuid4())
        try:
            cursor.execute(insert_query,
                           (user_id, row['name'], row['email'], row['age']))
        except mysql.connector.Error as err:
            print(f"Error inserting row {err}")
    connection.commit()
    print("Data inserted successfully")
    cursor.close()

if __name__ == "__main__":
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()

        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            insert_data(connection, 'user_data.csv')
            cursor = connection.cursor()
            cursor.execute(
                "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA " \
                "WHERE SCHEMA_NAME = 'ALX_prodev'")
            result = cursor.fetchone()
            if result:
                print("Database ALX_prodev is present")
            cursor.execute("SELECT * FROM user_data LIMIT 5;")
            rows = cursor.fetchall()
            print(rows)
            cursor.close()
