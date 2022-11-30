-- lists all shows, and all genres linked to that show
SELECT tv.`title`, tvg.`name`
FROM `tv_shows` AS tv
    LEFT JOIN `tv_show_genres` AS tvs
    ON tv.`id` = tvs.`show_id`

    LEFT JOIN `tv_genres` AS tvg
    ON tvg.`id` = tvs.`genre_id`
ORDER BY tv.`title` AND tvg.`name`;
