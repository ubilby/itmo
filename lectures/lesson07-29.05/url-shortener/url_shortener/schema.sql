CREATE TABLE IF NOT EXISTS shortener (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_url TEXT NOT NULL DEFAULT '',
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
