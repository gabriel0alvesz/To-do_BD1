USE lista_tarefas;

-- --------------------------------------- ----------------------------------------
-- Lista de Tarefas: Funções utilizadas no site
-- --------------------------------------------------------------------------------

# Contar linhas nas tabelas

SELECT COUNT(*) FROM usuario;
SELECT COUNT(*) FROM lista_de_tarefas;
SELECT COUNT(*) FROM tarefas;

# Buscar listas que o usuário tem acesso

SELECT l.id_lista, l.nome_descritivo, l.data_hora_criacao, l.data_hora_modificacao, l.responsavel_modificacao, l.fk_nome_usuario 
	FROM lista_de_tarefas AS l
	JOIN usuario AS u ON u.nome_usuario = l.fk_nome_usuario
	WHERE u.nome_usuario = 'gabriel'
UNION SELECT l.id_lista, l.nome_descritivo, l.data_hora_criacao, l.data_hora_modificacao, l.responsavel_modificacao, l.fk_nome_usuario 
	FROM lista_de_tarefas AS l
	JOIN convite AS c ON c.fk_lista_id = l.id_lista
	WHERE c.fk_nome_usuario_rec = 'gabriel'
		AND c.aceito = 1;
        
# Buscar convites pendentes

SELECT * 
	FROM convite AS c
    WHERE c.fk_nome_usuario_rec = 'teste'
		AND c.aceito = 0;
        
# Login de usuário

SELECT COUNT(*)
	FROM usuario AS u
    WHERE u.nome_usuario = 'teste'
		AND u.senha = 'pbkdf2_sha256$390000$qCWNq41e7pc1VYD6lliDwW$tkzEtcyZnkWk37mz6FaOmiUpXIeqXC0BzllExknD1dU=';
        
# Registrar usuário

INSERT INTO usuario (nome_usuario, email, nome, telefone, senha)
    VALUES ('henrique', 'henrique@henrique.com', 'Henrique', 99999999999,  'pbkdf2_sha256$390000$2ymu96OgveIeLatfA1kcdB$3+eT6XsfFekBlKMGPBv9rAI3f0ydeqrZv/GUiVxH18s=');
    
# Criar uma lista

INSERT INTO lista_de_tarefas (nome_descritivo, data_hora_criacao, data_hora_modificacao, responsavel_modificacao, fk_nome_usuario)
	VALUES ('Lista de teste', NOW(), NOW(), 'henrique', 'henrique');
    
# Buscar lista

SELECT *
	FROM lista_de_tarefas
    WHERE id_lista = 1;

# Buscar tarefas de uma lista

SELECT *
	FROM tarefas
    WHERE fk_lista_id = 1;

# Buscar usuários não convidados

SELECT *
	FROM usuario AS u
    LEFT JOIN (SELECT * from convite WHERE fk_lista_id = 1) AS c ON c.fk_nome_usuario_rec = u.nome_usuario
    WHERE u.nome_usuario != 'teste'
		AND c.id_convite IS NULL;
        
# Deletar uma lista

DELETE FROM lista_de_tarefas
	WHERE id_lista = 5;
    
# Criar um convite

INSERT INTO convite (fk_nome_usuario_env, fk_nome_usuario_rec, fk_lista_id)
	VALUES ('teste', 'henrique', 1);
    
# Responder um convite

SELECT *
	FROM convite AS c
    WHERE c.fk_lista_id = 1
		AND c.fk_nome_usuario_rec = 'henrique';
-- Recusado
DELETE FROM convite
	WHERE fk_lista_id = 1
		AND fk_nome_usuario_rec = 'henrique'; 
-- Aceito
UPDATE convite
SET aceito = 1
WHERE fk_lista_id = 1
		AND fk_nome_usuario_rec = 'henrique';


# Criar uma tarefa

UPDATE lista_de_tarefas
SET data_hora_modificacao = NOW(), responsavel_modificacao = 'henrique'
WHERE id_lista = 1;

INSERT INTO tarefas (descricao, data_cadastro, data_vencimento, tarefa_concluida, fk_lista_id)
	VALUES ('Nova Tarefa', NOW(), NOW(), 0, 1);
    
# Altera tarefa

START TRANSACTION;

SELECT *
	FROM tarefas
    WHERE id_tarefa = 11 FOR UPDATE;

UPDATE lista_de_tarefas
SET data_hora_modificacao = NOW(), responsavel_modificacao = 'henrique'
WHERE id_lista = 1;

-- Atualizar tarefa_concluida
UPDATE tarefas
SET tarefa_concluida = 1
WHERE id_tarefa = 10;
-- Delata tarefa
DELETE FROM tarefas
	WHERE id_tarefa = 10;
    
COMMIT;
    
# Atualizar dados da tarefa

START TRANSACTION;

SELECT *
	FROM tarefas
    WHERE id_tarefa = 11 FOR UPDATE;

UPDATE lista_de_tarefas
SET data_hora_modificacao = NOW(), responsavel_modificacao = 'henrique'
WHERE id_lista = 1;

UPDATE tarefas
SET descricao = 'nova tarefa', data_vencimento = NOW()
WHERE id_tarefa = 11;

COMMIT;