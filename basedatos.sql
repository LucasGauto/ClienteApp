CREATE DATABASE IF NOT EXISTS appCliente;
USE appCliente;

CREATE TABLE usuarios(
    usuarioID int identity(1,1) primary  key,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha date not null,
    CONSTRAINT uq_email UNIQUE(email) --campo unico
);