"""Create a generator that streams rows from an SQL database one by one."""
import mysql.connector


def stream_users():
    """Fetch rows one by one from the user_data table using a generator."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
