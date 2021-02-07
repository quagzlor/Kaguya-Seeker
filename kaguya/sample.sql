DROP DATABASE IF EXISTS kaguya;
DROP USER IF EXISTS students;
CREATE USER students WITH PASSWORD 'himitu';
CREATE DATABASE kaguya OWNER students;
\kaguya

DROP TABLE IF EXISTS ethnicity;
CREATE TABLE ethnicity (
id INTEGER PRIMARY KEY,
name TEXT,
code TEXT
);

DROP TABLE IF EXISTS continent;
Create TABLE continent (
id INTEGER PRIMARY KEY,
name TEXT,
code TEXT
);
