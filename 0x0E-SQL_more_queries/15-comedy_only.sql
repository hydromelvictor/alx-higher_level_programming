-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv.`title`
FROM `tv_shows` AS tv
    INNER JOIN `tv_show_genres` AS tvs
    ON tv.`id` = tvs.`show_id`

    INNER JOIN `tv_genres` AS tvg
    ON tv.`id` = tvs.`genre_id`
    WHERE tv.`title` = "Comedy"
ORDER BY tv.`title` ASC;
