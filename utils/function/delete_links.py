import sqlite3


def delete_all(id: int):
    conn = sqlite3.connect('config_data/database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM links WHERE id = ?', (id,))
    conn.commit()
    conn.close()
