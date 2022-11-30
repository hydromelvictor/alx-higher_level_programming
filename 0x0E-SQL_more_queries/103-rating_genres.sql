-- lists all genres in the database hbtn_0d_tvshows_rate
SELECT tvg.`name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS tvg
    INNER JOIN `tv_show_genres` AS tvs
    ON tvs.`genre_id` = tvg.`id`

    INNER JOIN `tv_show_rating` AS tvr
    ON tvs.`show_id` = tvr.`show_id`
GROUP BY tvg.`name`
ORDER BY `rating` DESC;
