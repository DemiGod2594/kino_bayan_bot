import sqlite3
from typing import List, Tuple


def get_all_messages() -> List[Tuple[int, str]]:
    conn = sqlite3.connect('config_data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, link FROM links')
    rows = cursor.fetchall()
    conn.close()
    return rows
