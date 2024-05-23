-- lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT s.title
FROM tv_shows s
INNER JOIN tv_show_genres t
ON s.id = t.show_id
INNER JOIN tv_genres g
ON g.id = t.genre_id
WHERE t.name = 'Comedy'
ORDER BY s.title;
