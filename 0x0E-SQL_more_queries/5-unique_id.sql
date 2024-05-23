-- creates the table unique_id on your MySQL server.
-- unique_id description:
-- id INT DEFAULT = 1
-- name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
