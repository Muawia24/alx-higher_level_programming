-- lists all shows contained in hbtn_0d_tvshows without genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT a.title, b.genre_id
FROM tv_show_genres b
	RIGHT JOIN tv_show a
	ON b.show_id = a.id
	WHERE b.genre_id IS NULL
ORDER BY a.title, b.genre_id;
