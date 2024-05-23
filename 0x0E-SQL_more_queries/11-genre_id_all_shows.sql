-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
SELECT s.title, g.genre_id
FROM tv_show s
	LEFT JOIN tv_show_genres g
	ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
