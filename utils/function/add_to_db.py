import sqlite3


def add_id_to_db(id):
    conn = sqlite3.connect('config_data/database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM links WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO links (id, link) VALUES (?, ?)', (id, ''))
        conn.commit()
    conn.close()


def add_message_to_id(id, link):
    conn = sqlite3.connect('config_data/database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT link FROM links WHERE id = ?', (id,))
    current_links = cursor.fetchone()
    if current_links:
        update_links = current_links[0] + '\n' + link
        cursor.execute('UPDATE links SET link = ? WHERE id = ?', (update_links, id))
        conn.commit()
    conn.close()

