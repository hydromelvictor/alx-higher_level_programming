-- lists all genres in the database hbtn_0d_tvshows_rate
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres`
    INNER JOIN `tv_show_genres` AS tvs
    ON tvs.`genre_id` = `id`

    INNER JOIN `tv_show_rating` AS tvr
    ON tvs.`show_id` = tvr.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
