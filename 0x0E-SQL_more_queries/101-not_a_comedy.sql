-- lists all shows without the genre Comedy in the database
SELECT DISTINCT tv.`title`
FROM `tv_shows` AS tv
    INNER JOIN `tv_show_genres` AS tvs
    ON tv.`id` = tvs.`show_id`

    INNER JOIN `tv_genres` AS tvg
    ON tv.`id` = tvs.`genre_id`
    WHERE tv.`title` NOT IN (
        SELECT tv.`title`
        FROM `tv_shows` AS tv
            INNER JOIN `tv_show_genres` AS tvs
            ON tv.`id` = tvs.`show_id`

            INNER JOIN `tv_genres` AS tvg
            ON tv.`id` = tvs.`genre_id`
            WHERE tv.`title` = "Comedy"
    )
ORDER BY tv.`title` ASC;
