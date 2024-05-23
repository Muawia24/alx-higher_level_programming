-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT g.name as 'name'
FROM tv_genres g
	INNER JOIN tv_show_genres t
	ON g.id = t.show_id
	JOIN INNER tv_shows s
	ON s.id = t.show_id
	WHERE s.title = 'Dexter'
ORDER BY g.name;
