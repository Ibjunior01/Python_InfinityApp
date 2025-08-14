CREATE DATABASE IF NOT EXISTS loja;

USE loja;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    quantidade INT,
    preco DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade INT,
    data_venda DATETIME,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);