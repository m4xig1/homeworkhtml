import sqlite3
conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
cursor = conn.cursor()
cursor.execute("""
SELECT
 (SELECT product_name FROM product_info WHERE product_id = sections.product_id) AS product_name,
 (SELECT description FROM product_info WHERE product_id = sections.product_id) AS description
  FROM sections
  WHERE sections.section_id = 2; -- название, описание по id 
  """)
print(cursor.fetchall())

cursor.execute("""
SELECT
 (SELECT product_name FROM product_info WHERE product_id = sections.product_id) AS product_name,
 (SELECT description FROM product_info WHERE product_id = sections.product_id) AS description
  FROM sections
  WHERE sections.section_id = (SELECT section_id FROM section_names WHERE section_name = 'Электроника'); -- название, описание товара по названию раздела
""")
print(cursor.fetchall())

cursor.execute("""
SELECT 
  section_name AS 'Название раздела' FROM section_names 
  WHERE section_id = (SELECT section_id FROM sections WHERE product_id = 3)
""")
print(cursor.fetchall())

cursor.execute("""
SELECT 
  product_name, max(price) FROM product_info
 UNION 
 SELECT
 product_name, min(price) FROM product_info;
""")
print(cursor.fetchall())

cursor.execute("""
SELECT * 
  FROM product_info JOIN sections
  ON product_info.product_id = sections.product_id; -- объединение описания товара и id его секции
""")
print(cursor.fetchall())

conn.close()
