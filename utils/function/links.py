import sqlite3


def get_info_by_id(id):
    conn = sqlite3.connect('config_data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT link FROM links WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Ссылка не найдена"

