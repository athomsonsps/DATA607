-- DATA 607 Week 2
--

-- Six anonymous participant records, where they selected family movies and rated them
-- and runs the queries used in the report.

PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id        INTEGER PRIMARY KEY,
    participant_id TEXT NOT NULL UNIQUE
);

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title    TEXT NOT NULL UNIQUE
);

CREATE TABLE ratings (
    user_id  INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating   INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO users (user_id, participant_id) VALUES
    (1, 'Participant 1'),
    (2, 'Participant 2'),
    (3, 'Participant 3'),
    (4, 'Participant 4'),
    (5, 'Participant 5'),
    (6, 'Participant 6');

INSERT INTO movies (movie_id, title) VALUES
    (1, 'Puss in Boots: The Last Wish'),
    (2, 'The Wild Robot'),
    (3, 'Inside Out 2'),
    (4, 'Moana 2'),
    (5, 'Dog Man'),
    (6, 'The Super Mario Bros. Movie');

-- Ratings copied from the anonymous Google Form responses.
-- If a participant leaves a movie blank, omit that participant/movie row.
INSERT INTO ratings (user_id, movie_id, rating) VALUES
    (1, 1, 5), (1, 2, 5), (1, 3, 5), (1, 4, 5), (1, 5, 3), (1, 6, 4),
    (2, 1, 5), (2, 2, 5), (2, 3, 3), (2, 4, 5), (2, 5, 2), (2, 6, 4),
    (3, 1, 3), (3, 2, 2), (3, 3, 1), (3, 4, 2), (3, 5, 5), (3, 6, 5),
    (4, 1, 3), (4, 2, 5), (4, 3, 2), (4, 4, 3), (4, 5, 4), (4, 6, 5),
    (5, 1, 5), (5, 2, 4), (5, 3, 1), (5, 4, 1), (5, 5, 1), (5, 6, 5),
    (6, 1, 5), (6, 2, 5), (6, 3, 3), (6, 4, 3), (6, 5, 2), (6, 6, 5);

COMMIT;

-- Verification of the expected values are 6 participants, 6 movies, and 36 ratings.
SELECT COUNT(*) AS participant_count FROM users;
SELECT COUNT(*) AS movie_count FROM movies;
SELECT COUNT(*) AS rating_count FROM ratings;

-- Tidy participant, movie, rating result used by R.
SELECT
    u.participant_id,
    m.title AS movie_title,
    r.rating
FROM ratings AS r
INNER JOIN users AS u ON r.user_id = u.user_id
INNER JOIN movies AS m ON r.movie_id = m.movie_id
ORDER BY u.user_id, m.movie_id;

-- The number of ratings and average rating for each movie.
SELECT
    m.title AS movie_title,
    COUNT(r.rating) AS number_of_ratings,
    ROUND(AVG(r.rating), 2) AS average_rating
FROM movies AS m
LEFT JOIN ratings AS r ON m.movie_id = r.movie_id
GROUP BY m.movie_id, m.title
ORDER BY average_rating DESC, m.title;

-- The number of completed ratings for each participant.
SELECT
    u.participant_id,
    COUNT(r.rating) AS number_of_ratings
FROM users AS u
LEFT JOIN ratings AS r ON u.user_id = r.user_id
GROUP BY u.user_id, u.participant_id
ORDER BY u.user_id;

-- The missing ratings and the unseen movie has no ratings row; it is never stored as 0.
SELECT
    u.participant_id,
    m.title AS movie_title
FROM users AS u
CROSS JOIN movies AS m
LEFT JOIN ratings AS r
    ON r.user_id = u.user_id
   AND r.movie_id = m.movie_id
WHERE r.rating IS NULL
ORDER BY u.user_id, m.movie_id;
