import sqlite3
from loader import db


def get_info_by_id(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT link FROM links WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Информация не найдена"

