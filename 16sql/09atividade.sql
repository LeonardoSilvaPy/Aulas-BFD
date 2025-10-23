-- Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas.
-- (Use GROUP BY e HAVING)

SELECT ano, COUNT(*) AS quantidade_turmas
FROM turma
GROUP BY ano
HAVING COUNT(*) > 2;
