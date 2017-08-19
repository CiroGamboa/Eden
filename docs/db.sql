BEGIN TRANSACTION;
CREATE TABLE `libroUser` (
	`user`	INTEGER,
	`libro`	INTEGER,
	FOREIGN KEY(`user`) REFERENCES User(id),
	FOREIGN KEY(`libro`) REFERENCES Libro(id)
);
CREATE TABLE `User` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`pass`	TEXT NOT NULL,
	`nombre`	TEXT NOT NULL,
	`correo`	TEXT NOT NULL,
	`pais`	TEXT,
	`ciudad`	TEXT,
	`cumpleaños`	TEXT
);
CREATE TABLE `Planta` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	TEXT NOT NULL
);
CREATE TABLE "Maceta" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`tipoPlanta`	INTEGER,
	`fechaDePlantacion`	TEXT,
	`primeraCosecha`	TEXT,
	`user`	INTEGER,
	FOREIGN KEY(`tipoPlanta`) REFERENCES `Planta`(`id`),
	FOREIGN KEY(`user`) REFERENCES `User`(`id`)
);
CREATE TABLE `LogValvula` (
	`maceta`	INTEGER,
	`fecha`	TEXT,
	`cant`	INTEGER,
	FOREIGN KEY(`maceta`) REFERENCES Maceta(id)
);
CREATE TABLE `LogTemperatura` (
	`maceta`	INTEGER,
	`fecha`	TEXT,
	`cant`	INTEGER,
	PRIMARY KEY(maceta,fecha),
	FOREIGN KEY(`maceta`) REFERENCES Maceta(id)
);
CREATE TABLE `LogLuminocidad` (
	`maceta`	INTEGER,
	`fecha`	TEXT,
	`cant`	INTEGER,
	FOREIGN KEY(`maceta`) REFERENCES Maceta(id)
);
CREATE TABLE `LogHumedad` (
	`maceta`	INTEGER,
	`fecha`	TEXT,
	`cant`	INTEGER,
	PRIMARY KEY(maceta,fecha),
	FOREIGN KEY(`maceta`) REFERENCES Maceta(id)
);
CREATE TABLE `Libro` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	TEXT NOT NULL,
	`cuerpo`	TEXT NOT NULL,
	`autor`	TEXT NOT NULL,
	`precio`	INTEGER NOT NULL,
	`editorial`	TEXT,
	`fechaDePubli`	TEXT
);
CREATE TABLE `Foto` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`fotoURL`	TEXT NOT NULL,
	`user`	INTEGER NOT NULL,
	FOREIGN KEY(`user`) REFERENCES User(id)
);
COMMIT;
