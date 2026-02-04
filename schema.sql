-- Enable foreign key constraints in SQLite
PRAGMA foreign_keys = ON;

-- ======================
-- User table
-- ======================
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL
);