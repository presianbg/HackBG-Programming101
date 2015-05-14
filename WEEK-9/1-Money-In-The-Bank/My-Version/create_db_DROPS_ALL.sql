DROP TABLE IF EXISTS clients;

CREATE TABLE IF not exists clients(
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    balance REAL DEFAULT 0,
    message TEXT);
