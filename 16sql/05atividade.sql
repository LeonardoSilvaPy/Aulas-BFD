-- Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais. 
-- (Use WHERE com condição numérica)

SELECT nome, mensalidade
FROM curso
WHERE mensalidade > 600;
