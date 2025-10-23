-- Liste o ano das turmas e a quantidade de turmas por ano. (Use GROUP BY)

SELECT ano, COUNT(*) AS quantidade_turmas
FROM turma
GROUP BY ano;
