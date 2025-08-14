# import mysql.connector

# def conectar():
#     return mysql.connector.connect(
#         host="localhost",
#         user="seu_usuario",
#         password="sua_senha",
#         database="loja"
#     )

import sqlite3

def conectar():
    return sqlite3.connect("estoque.db")