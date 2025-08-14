from db import get_conn
from pathlib import Path

SQL_SCHEMA = (Path(__file__).parent / "schema.sql").read_text(encoding="utf-8")

with get_conn() as conn:
    # Criar as tabelas
    conn.executescript(SQL_SCHEMA)

    # Inserir dados exemplo
    conn.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", ("Ana", 20))
    conn.execute("INSERT INTO cursos (nome_curso, carga_horaria) VALUES (?, ?)", ("SQL Básico", 40))
    conn.execute(
        "INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (?, ?, ?)",
        (1, 1, "2025-08-14")
    )
    conn.commit()
