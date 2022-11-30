-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tvg.`name`
FROM `tv_genres` AS tvg 
    INNER JOIN `tv_show_genre` AS tvs
    ON tvs.`id` = tvs.`genre_id`

    INNER JOIN `tv_shows` AS tv
    ON tv.`id` = tvs.`show_id`
    WHERE tvs.`title` = "Dexter"
ORDER BY tvg.`name` ASC;
