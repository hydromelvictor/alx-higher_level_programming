-- uses the hbtn_0d_tvshows database to list all genres
SELECT DISTINCT tvg.`name`
FROM `tv_genres` AS tvg
    INNER JOIN `tv_show_genres` AS tvs
    ON tvg.`id` = tvs.`genre_id`

    INNER JOIN `tv_shows` AS tv
    ON tv.`id` = tvs.`show_id`
    WHERE tv.`name` NOT IN (
        SELECT tvg.`name`
        FROM `tv_genres` AS tvg
            INNER JOIN `tv_show_genres` AS tvs
            ON tvg.`id` = tvs.`genre_id`

            INNER JOIN `tv_shows` AS tv
            ON tv.`id` = tvs.`show_id`
            WHERE tv.`name` = "Dexter"
    )
ORDER BY tvg.`name` ASC;
