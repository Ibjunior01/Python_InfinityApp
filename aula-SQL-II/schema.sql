-- =========================
-- Atividade 01
-- 1) Tabela pedidos com chave estrangeira
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data_pedido TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- 2) Tabela produtos com preço > 0
CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco > 0)
);

-- 3) Adicionar constraint UNIQUE em email da tabela clientes
CREATE UNIQUE INDEX IF NOT EXISTS idx_clientes_email
ON clientes(email);

-- 4) Consulta de alunos > 20 anos matriculados em Matemática
-- (Este é só o SELECT, não cria nada)
-- SELECT nome
-- FROM alunos
-- WHERE idade > 20
-- AND id_aluno IN (
--     SELECT m.id_aluno
--     FROM matriculas m
--     JOIN cursos c ON m.id_curso = c.id_curso
--     WHERE c.nome_curso = 'Matemática'
-- );

-- =========================
-- Desafio 01: Loja Online
-- =========================

CREATE TABLE IF NOT EXISTS produtos_loja (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco > 0),
    quantidade INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS clientes_loja (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    email_cliente TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos_loja (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    data_pedido TEXT NOT NULL,
    id_cliente INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes_loja(id_cliente)
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos_loja(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos_loja(id_produto)
);

-- Consultas e operações
-- a) Selecionar todos clientes
-- SELECT * FROM clientes_loja;

-- b) Inserir produto Notebook
-- INSERT INTO produtos_loja (nome_produto, preco, quantidade) VALUES ('Notebook', 2500.00, 10);

-- c) Atualizar nome do cliente id=1
-- UPDATE clientes_loja SET nome_cliente = 'Maria Silva' WHERE id_cliente = 1;

-- d) Remover vendas antes de 01/01/2023
-- DELETE FROM pedidos_loja WHERE data_pedido < '2023-01-01';

-- =========================
-- Desafio 02
-- =========================
CREATE TABLE IF NOT EXISTS produtos_teste (
    ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeProduto TEXT NOT NULL,
    Quantidade INTEGER NOT NULL,
    Preco REAL NOT NULL CHECK (Preco > 0)
);
