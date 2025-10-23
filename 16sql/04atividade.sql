-- Mostre os alunos que nasceram após o ano de 2000. (Use WHERE com data)

SELECT *
FROM Aluno
WHERE data_nascimento > '2000-12-31';
