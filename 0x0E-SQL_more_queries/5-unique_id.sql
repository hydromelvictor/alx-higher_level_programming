-- creates the table  on your MySQL
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT    DEFAULT 1   UNIQUE,
    `name` VARCHAR(256)
);
