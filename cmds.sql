SELECT CURRENT_DATE;
UPDATE product_info SET last_update = SUBSTR(last_update, 1, 4) || '-' || SUBSTR(last_update, 6, 2) || '-' ||SUBSTR(last_update, 9, 2); -- изменить формат даты
INSERT INTO 'product_info' (last_update) VALUES (CURRENT_DATE);
SELECT product_id, MAX(CAST(strftime('%s', last_update)  AS  integer)) FROM product_info; -- найти последний измененный продукт
SELECT * FROM product_info WHERE product_id = 1; -- вывести информацию по id
SELECT product_id, COUNT(*) AS 'total_items' from product_info; -- вывести общее кол-во предметов
SELECT AVG(price) AS 'avg. price' FROM product_info WHERE (CAST(strftime('%s', CURRENT_DATE) AS integer) - CAST(strftime('%s', last_update)  AS  integer)) < 5259487; -- средняя цена товаров, добавленных не позже 2 месяцев