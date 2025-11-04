"""Generator to compute a memory-efficient aggregate function."""
from seed import connect_to_prodev

def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = connect_to_prodev()
    if not connection:
        return
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    try:
        for (age,) in cursor:
            yield age
    finally:
        cursor.close()
        connection.close()

def average_age():
    """Compute average age using generator without loading all data."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        print(f"Average age of users: {total / count:.2f}")
    else:
        print("No users found.")
