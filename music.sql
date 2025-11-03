-- Drop tables if they already exist (for resetting)
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;

-- Create Artist table
CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Create Album table
CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

-- Create Song table
CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    duration_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id)
);

-- Sample data for testing

-- Artists
INSERT INTO artist (name) VALUES ('The Beatles');
INSERT INTO artist (name) VALUES ('Taylor Swift');

-- Albums
INSERT INTO album (name, artist_id) VALUES ('Abbey Road', 1);
INSERT INTO album (name, artist_id) VALUES ('1989', 2);

-- Songs
INSERT INTO song (name, album_id, track_number, duration_seconds)
VALUES ('Come Together', 1, 1, 259);
INSERT INTO song (name, album_id, track_number, duration_seconds)
VALUES ('Something', 1, 2, 182);
INSERT INTO song (name, album_id, track_number, duration_seconds)
VALUES ('Blank Space', 2, 1, 231);
INSERT INTO song (name, album_id, track_number, duration_seconds)
VALUES ('Style', 2, 2, 231);

