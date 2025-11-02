"""Create a generator that streams rows from an SQL database one by one."""
from seed import connect_to_prodev


def stream_users():
    """Fetch rows one by one from the user_data table using a generator."""
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

        cursor.close()
        connection.close()
