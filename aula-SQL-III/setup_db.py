import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Clientes e Pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome_cliente TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id INTEGER PRIMARY KEY,
    numero_pedido TEXT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
)
""")

# Vendedores e Vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendedores (
    vendedor_id INTEGER PRIMARY KEY,
    nome_vendedor TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    venda_id INTEGER PRIMARY KEY,
    valor REAL,
    vendedor_id INTEGER,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(vendedor_id)
)
""")

# Pessoas e Documentos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    pessoa_id INTEGER PRIMARY KEY,
    nome TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS documentos (
    documento_id INTEGER PRIMARY KEY,
    tipo TEXT,
    pessoa_id INTEGER,
    FOREIGN KEY (pessoa_id) REFERENCES pessoas(pessoa_id)
)
""")

# Autores e Livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    autor_id INTEGER PRIMARY KEY,
    nome_autor TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    livro_id INTEGER PRIMARY KEY,
    titulo TEXT,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
)
""")

# Músicos e Bandas
cursor.execute("""
CREATE TABLE IF NOT EXISTS musicos (
    musico_id INTEGER PRIMARY KEY,
    nome_musico TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS bandas (
    banda_id INTEGER PRIMARY KEY,
    nome_banda TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS musicos_bandas (
    musico_id INTEGER,
    banda_id INTEGER,
    FOREIGN KEY (musico_id) REFERENCES musicos(musico_id),
    FOREIGN KEY (banda_id) REFERENCES bandas(banda_id)
)
""")

# Biblioteca (Desafio 01)
cursor.execute("""
CREATE TABLE IF NOT EXISTS editoras (
    editora_id INTEGER PRIMARY KEY,
    nome_editora TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros_editora (
    livro_id INTEGER,
    editora_id INTEGER,
    FOREIGN KEY (livro_id) REFERENCES livros(livro_id),
    FOREIGN KEY (editora_id) REFERENCES editoras(editora_id)
)
""")

# Estoque (Desafio 02)
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INTEGER PRIMARY KEY,
    nome_produto TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS estoque (
    estoque_id INTEGER PRIMARY KEY,
    quantidade INTEGER,
    produto_id INTEGER,
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
)
""")

conn.commit()
conn.close()