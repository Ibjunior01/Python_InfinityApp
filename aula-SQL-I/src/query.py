from db import get_conn
import pandas as pd

with get_conn() as conn:
    # Consultar alunos
    alunos = conn.execute("SELECT * FROM alunos").fetchall()
    for aluno in alunos:
        print(dict(aluno))

    # Usar pandas para mostrar join
    df = pd.read_sql("""
        SELECT a.nome, c.nome_curso, m.data_matricula
        FROM matriculas m
        JOIN alunos a ON m.id_aluno = a.id_aluno
        JOIN cursos c ON m.id_curso = c.id_curso
    """, conn)
    print(df)
