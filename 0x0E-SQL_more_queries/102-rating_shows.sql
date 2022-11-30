-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv.`title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS tv 
    INNER JOIN `tv_show_ratings` AS tvrs
    ON tv.`id` = tvrs.`show_id`
GROUP BY tv.`title`
ORDER BY `rating` DESC;
