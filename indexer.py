import sqlite3
import os

def create_table():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/documents.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS documents (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              url TEXT,
              content TEXT    
        )
    ''')
    conn.commit()
    conn.close()

def insert_document(title, url, content):
    conn = sqlite3.connect("data/documents.db")
    c = conn.cursor()
    c.execute("INSERT INTO documents (title, url, content) VALUES (?, ?, ?)", (title, url, content))
    conn.commit()
    conn.close()