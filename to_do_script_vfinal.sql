CREATE DATABASE IF NOT EXISTS lista_tarefas;

USE lista_tarefas;

 -- SHOW DATABASES;

# Lista de Tarefas

CREATE TABLE Usuario (
    nome_usuario VARCHAR(20) PRIMARY KEY,
    senha VARCHAR(64) NOT NULL,
    nome VARCHAR(60) NOT NULL,
    telefone INTEGER NOT NULL,
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
    aceito BOOL DEFAULT(FALSE) NOT NULL,
    fk_nome_usuario_env VARCHAR(20) NOT NULL,
    fk_nome_usuario_rec VARCHAR(20) NOT NULL,
    fk_lista_id INTEGER NOT NULL,
    FOREIGN KEY (fk_nome_usuario_env) REFERENCES Usuario (nome_usuario),
    FOREIGN KEY (fk_nome_usuario_rec) REFERENCES Usuario (nome_usuario),
    FOREIGN KEY (fk_lista_id) REFERENCES Lista_de_Tarefas (id_lista)
);

CREATE TABLE Tarefas (
    id_tarefa INTEGER AUTO_INCREMENT PRIMARY KEY,
    data_cadastro DATETIME NOT NULL, 
    data_vencimento DATETIME NULL,
    tarefa_concluida BOOL DEFAULT(FALSE) NOT NULL,
    fk_lista_id INTEGER NOT NULL,
    FOREIGN KEY (fk_lista_id) REFERENCES Lista_de_Tarefas (id_lista)
);