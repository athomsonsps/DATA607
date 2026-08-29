-- Week 2A Assignment: SQL and R - Movie Ratings
-- Author: Your Name
-- Date: February 9, 2026
-- Course: DATA 607

-- This SQL script creates a normalized database for storing movie ratings
-- Using SQLite syntax (compatible with PostgreSQL with minor modifications)

-- Drop tables if they exist (for reproducibility)
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create movies table
CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    genre TEXT
);

-- Create ratings table (junction table for many-to-many relationship)
CREATE TABLE ratings (
    rating_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- Insert users (5 people who provided ratings)
INSERT INTO users (user_id, name) VALUES
(1, 'Alice Johnson'),
(2, 'Bob Smith'),
(3, 'Carol Williams'),
(4, 'David Brown'),
(5, 'Emma Davis');

-- Insert movies (6 recent popular movies from Feb 2026)
INSERT INTO movies (movie_id, title, year, genre) VALUES
(1, 'Send Help', 2026, 'Horror/Thriller'),
(2, 'Primate', 2026, 'Action'),
(3, '28 Years Later: The Bone Temple', 2026, 'Horror'),
(4, 'Mercy', 2026, 'Thriller'),
(5, 'Iron Lung', 2026, 'Horror'),
(6, 'Greenland 2: Migration', 2026, 'Action/Thriller');

-- Insert ratings (with some missing values to demonstrate handling missing data)
-- Note: Not all users have seen all movies
INSERT INTO ratings (rating_id, user_id, movie_id, rating) VALUES
-- Send Help ratings
(1, 1, 1, 4),
(2, 2, 1, 5),
(3, 3, 1, 3),
(4, 4, 1, 4),
(5, 5, 1, 5),

-- Primate ratings (Bob hasn't seen it)
(6, 1, 2, 3),
(7, 3, 2, 4),
(8, 4, 2, 3),
(9, 5, 2, 4),

-- 28 Years Later ratings (Carol and Emma haven't seen it)
(10, 1, 3, 5),
(11, 2, 3, 4),
(12, 4, 3, 5),

-- Mercy ratings (Alice hasn't seen it)
(13, 2, 4, 3),
(14, 3, 4, 4),
(15, 4, 4, 3),
(16, 5, 4, 4),

-- Iron Lung ratings (David and Emma haven't seen it)
(17, 1, 5, 4),
(18, 2, 5, 5),
(19, 3, 5, 4),

-- Greenland 2 ratings (Alice and Bob haven't seen it)
(20, 3, 6, 5),
(21, 4, 6, 4),
(22, 5, 6, 5);

-- Verify the data
SELECT 'Users:' as table_name, COUNT(*) as count FROM users
UNION ALL
SELECT 'Movies:', COUNT(*) FROM movies
UNION ALL
SELECT 'Ratings:', COUNT(*) FROM ratings;

-- View complete rating data with joins
SELECT 
    u.name as user_name,
    m.title as movie_title,
    r.rating
FROM ratings r
JOIN users u ON r.user_id = u.user_id
JOIN movies m ON r.movie_id = m.movie_id
ORDER BY u.name, m.title;
