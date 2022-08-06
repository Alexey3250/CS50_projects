SELECT ROUND(AVG(rating), 2) AS Average_rating
FROM ratings
WHERE movie_id IN
        (SELECT id
        FROM movies
        WHERE year = 2012);