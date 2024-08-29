import sqlite3


def init_db():
    conn = sqlite3.connect('config_data/database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links
                 (id INTEGER PRIMARY KEY, link TEXT)''')
    conn.commit()
    conn.close()