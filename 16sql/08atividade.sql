-- Calcule a média da nota1 dos alunos por turma_id. (Use GROUP BY com função de agregação)

SELECT id_turma, AVG(nota1) AS media_nota1
FROM Aluno
GROUP BY id_turma;

