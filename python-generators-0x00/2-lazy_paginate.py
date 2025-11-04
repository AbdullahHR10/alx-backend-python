"""Simulte fetching paginated data from the users database
using a generator to lazily load each page."""
from seed import connect_to_prodev


def paginate_users(page_size, offset):
    """Fetch one page of users from the database."""
    connection = connect_to_prodev()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}"
    )
    rows = cursor.fetchall()

    cursor.close()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """Generator that lazily loads each page."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
