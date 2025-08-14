# src/db.py
import sqlite3
import os

# Caminho do banco de dados (será criado na pasta raiz do projeto)
DB_PATH = os.path.join(os.path.dirname(__file__), "loja.db")

def get_conn():
    """Retorna uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(DB_PATH)
