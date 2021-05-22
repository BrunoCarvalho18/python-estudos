import sqlite3

conn = sqlite3.connect("cafe.db")

cursor = conn.cursor()

SQL = """
      CREATE TABLE ingrediente(
          id integer primary key autoincrement,
          nome text,
          descricao text,
          tipo text,
          unidade_medida text
      );
"""

cursor.execute(SQL)