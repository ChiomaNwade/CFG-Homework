-- CFG FOUNDATION ASSESSMENT 2
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

-- Create the movie_info table
CREATE TABLE movie_info (
  Movie_ID INT PRIMARY KEY,
  Movie_Name VARCHAR(100),
  Movie_Length TIME,
  Age_Rating VARCHAR(10)
);

-- Insert data into the movie_info table
INSERT INTO movie_info (Movie_ID, Movie_Name, Movie_Length, Age_Rating)
VALUES
  (1, 'The Movie', '02:19:00', '12A'),
  (2, 'The Other Movie', '01:30:00', '15'),
  (3, 'The 3D Amazing Movie', '01:42:00', 'PG'),
  (4, 'La Allure', '01:09:00', '18'),
  (5, 'The Cartoon', '01:15:00', 'U'),
  (6, 'The Scary Cartoon', '01:23:00', 'PG'),
  (7, 'The Coming Of Age', '01:40:00', '12A'),
  (8, 'The War', '02:07:00', '15'),
  (9, 'The Murder Mystery', '01:47:00', '15');

-- Create the screens table
CREATE TABLE screens (
  Screen_ID INT PRIMARY KEY,
  Four_K BOOLEAN
);

-- Insert data into the screens table
INSERT INTO screens (Screen_ID, Four_K)
VALUES
  (1, TRUE),
  (2, FALSE),
  (3, TRUE),
  (4, TRUE),
  (5, TRUE),
  (6, TRUE),
  (7, TRUE),
  (8, FALSE),
  (9, TRUE),
  (10, TRUE);

-- Create the showings table
CREATE TABLE showings (
  Showing_ID INT PRIMARY KEY,
  Movie_ID INT,
  Screen_ID INT,
  Start_Time TIME,
  Available_Seats INT
);

-- Insert data into the showings table
INSERT INTO showings (Showing_ID, Movie_ID, Screen_ID, Start_Time, Available_Seats)
VALUES
  (1, 1, 2, '12:00:00', 10),
  (2, 1, 2, '17:00:00', 23),
  (3, 2, 9, '10:30:00', 30),
  (4, 3, 1, '07:00:00', 38),
  (5, 3, 5, '10:00:00', 26),
  (6, 3, 1, '17:00:00', 5),
  (7, 3, 1, '19:00:00', 0),
  (8, 3, 5, '14:00:00', 2),
  (9, 4, 9, '20:00:00', 14),
  (10, 4, 9, '23:00:00', 23),
  (11, 5, 6, '09:30:00', 30),
  (12, 5, 6, '12:30:00', 7),
  (13, 5, 6, '14:30:00', 0),
  (14, 5, 6, '15:20:00', 0),
  (15, 6, 10, '10:00:00', 32),
  (16, 6, 10, '13:30:00', 25),
  (17, 6, 10, '17:00:00', 14),
  (18, 7, 7, '12:00:00', 36),
  (19, 8, 4, '15:00:00', 24),
  (20, 9, 3, '17:00:00', 0);

-- name and time of all movies that play after 12:00 given there is at least 1 available seat. Display the results in time order.


SELECT Movie_Name, Movie_Length
FROM movie_info
JOIN showings ON movie_info.Movie_ID = showings.Movie_ID
WHERE Start_Time > '12:00:00' AND Available_Seats > 0
ORDER BY Start_Time;

-- movie with most showings
SELECT Movie_Name
FROM movie_info
JOIN showings ON movie_info.Movie_ID = showings.Movie_ID
GROUP BY movie_info.Movie_ID, movie_info.Movie_Name
ORDER BY COUNT(*) DESC
LIMIT 1;


