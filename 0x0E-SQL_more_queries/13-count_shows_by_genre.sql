-- lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tv_g
ON g.id = tv_g.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
