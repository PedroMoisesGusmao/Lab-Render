CREATE DATABASE movies;

\c movies;

CREATE TABLE movies (
  name   VARCHAR(255),
  rating NUMERIC
);

INSERT INTO movies VALUES ('The Dark Knight', 8.1);
INSERT INTO movies VALUES ('Os Observadores', 5.7);
INSERT INTO movies VALUES ('The Matrix', 9.9);
INSERT INTO movies VALUES ('The Lord of the Rings', 11.0);
INSERT INTO movies VALUES ('Star Wars', 3.4);
INSERT INTO movies VALUES ('Donzela', 4.5);
INSERT INTO movies VALUES ('Bad Boys 4.0', 10.0);
INSERT INTO movies VALUES ('Gladiator', 1.1);
INSERT INTO movies VALUES ('Logan', 8.5);
