-- Atividade 01: criar banco e tabelas
CREATE TABLE IF NOT EXISTS alunos (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
);

CREATE TABLE IF NOT EXISTS cursos (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso TEXT NOT NULL,
    carga_horaria INTEGER
);

CREATE TABLE IF NOT EXISTS matriculas (
    id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    data_matricula TEXT NOT NULL,
    FOREIGN KEY(id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY(id_curso) REFERENCES cursos(id_curso)
);

-- Desafio prático: sistema da escola
CREATE TABLE IF NOT EXISTS professores (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    especialidade TEXT,
    endereco TEXT
);

CREATE TABLE IF NOT EXISTS turmas (
    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
    horario_inicio TEXT,
    dia_semana TEXT
);

CREATE TABLE IF NOT EXISTS disciplinas (
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    qtd_aulas INTEGER
);

-- Desafio 2: tabela Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Idade INTEGER,
    Cidade TEXT
);

with get_conn() as conn:
    conn.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", ("João", 30, "São Paulo"))
    conn.commit()
