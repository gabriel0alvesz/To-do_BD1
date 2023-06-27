CREATE DATABASE IF NOT EXISTS lista_tarefas;

USE lista_tarefas;
-- --------------------------------------------------------------------------------
-- Lista de Tarefas: Definição das Tabelas
-- --------------------------------------------------------------------------------

CREATE TABLE Usuario (
    nome_usuario VARCHAR(20) PRIMARY KEY,
    senha VARCHAR(100) NOT NULL,
    nome VARCHAR(60) NOT NULL,
    telefone BIGINT NOT NULL,
    email VARCHAR(60) NOT NULL
);

CREATE TABLE Lista_de_Tarefas (
    id_lista INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome_descritivo VARCHAR(60) NOT NULL,
    data_hora_criacao DATETIME NOT NULL,
    data_hora_modificacao DATETIME NOT NULL,
    responsavel_modificacao VARCHAR(20) NOT NULL,
    fk_nome_usuario VARCHAR(20) NOT NULL,
    FOREIGN KEY (fk_nome_usuario) REFERENCES Usuario(nome_usuario)
);

CREATE TABLE Convite (
    id_convite INTEGER AUTO_INCREMENT PRIMARY KEY,
    aceito BOOL DEFAULT(FALSE) NOT NULL,
    fk_nome_usuario_env VARCHAR(20) NOT NULL,
    fk_nome_usuario_rec VARCHAR(20) NOT NULL,
    fk_lista_id INTEGER NOT NULL,
    FOREIGN KEY (fk_nome_usuario_env) REFERENCES Usuario (nome_usuario),
    FOREIGN KEY (fk_nome_usuario_rec) REFERENCES Usuario (nome_usuario),
    FOREIGN KEY (fk_lista_id) REFERENCES Lista_de_Tarefas (id_lista) ON DELETE CASCADE
);

CREATE TABLE Tarefas (
    id_tarefa INTEGER AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    data_cadastro DATETIME NOT NULL, 
    data_vencimento DATETIME NULL,
    tarefa_concluida BOOL DEFAULT(FALSE) NOT NULL,
    fk_lista_id INTEGER NOT NULL,
    FOREIGN KEY (fk_lista_id) REFERENCES Lista_de_Tarefas (id_lista) ON DELETE CASCADE
);

-- --------------------------------------------------------------------------------
-- Lista de Tarefas: Inserção de Dados para Teste
-- --------------------------------------------------------------------------------

# Usuários de teste

INSERT INTO usuario (nome_usuario, senha, nome, telefone, email) VALUES
	('gabriel', 'pbkdf2_sha256$390000$2Yht4sfe8xMUQ7vApyslqk$h1rbAk3CXwQZaogK66HK+NtJmuI2nbIuw9mE3rZe4CY=', 'Gabriel', 1234, 'gabriel@gabriel'),
    ('pedro', 'pbkdf2_sha256$390000$NWLuVQ9koM1Qv42n3B9D2u$FqdytTxfQL+694wUJfyf5EMwGo2BT5YMAp3VLnhUhTQ=', 'Pedro', 5678, 'pedro@pedro'),
    ('teste', 'pbkdf2_sha256$390000$qCWNq41e7pc1VYD6lliDwW$tkzEtcyZnkWk37mz6FaOmiUpXIeqXC0BzllExknD1dU=', 'Teste', 9012, 'teste@teste');

# Listas de teste

INSERT INTO lista_de_tarefas (nome_descritivo, data_hora_criacao, data_hora_modificacao, responsavel_modificacao, fk_nome_usuario) VALUES
	('Lista de gabriel', NOW(), NOW(), 'gabriel', 'gabriel'),
    ('Lista de pedro', NOW(), NOW(), 'pedro', 'pedro'),
    ('Lista de teste', NOW(), NOW(), 'teste', 'teste');

# Tarefas de teste

INSERT INTO tarefas (descricao, data_cadastro, tarefa_concluida, fk_lista_id) VALUES
	('Tarefa', NOW(), 0, 1),
    ('Tarefa', NOW(), 0, 2),
    ('Tarefa 1', NOW(), 0, 3);

INSERT INTO tarefas (descricao, data_cadastro, data_vencimento, tarefa_concluida, fk_lista_id) VALUES
    ('Tarefa 2', NOW(), NOW(), 0, 1);
    
# Convite de teste

INSERT INTO convite (aceito, fk_nome_usuario_env, fk_nome_usuario_rec, fk_lista_id)
	VALUES (1, 'teste', 'gabriel', 3);
