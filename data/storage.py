import sqlite3


def init_db():
    conn = sqlite3.connect('chats.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()


def add_chat(chat_id):
    conn = sqlite3.connect('chats.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO chats (chat_id)
            VALUES (?)
        ''', (chat_id,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def get_all_chats():
    conn = sqlite3.connect('chats.db')
    cursor = conn.cursor()
    cursor.execute('SELECT chat_id FROM chats')
    chats = cursor.fetchall()
    conn.close()
    return [chat[0] for chat in chats]