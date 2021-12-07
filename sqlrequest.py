from os import close
import sqlite3
#conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
#cursor = conn.cursor()
#conn.close()


def get_name_from_id(id): # 1 2 3
  conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
  cursor = conn.cursor()
  cursor.execute(f"""
  SELECT section_id,
	(SELECT product_name FROM product_info WHERE product_info.product_id = sections.product_id),
	(SELECT description FROM product_info WHERE product_info.product_id = sections.product_id)
	FROM sections
	WHERE sections.product_id = {id};  -- название, описание по id  
    """)
  f = cursor.fetchone()
  conn.close()
  return f


def get_name_from_section(section_name): # 'Электроника', 'Другое'
  conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
  cursor = conn.cursor()
  cursor.execute(f"""
  SELECT
  (SELECT product_name FROM product_info WHERE product_id = sections.product_id) AS product_name,
  (SELECT description FROM product_info WHERE product_id = sections.product_id) AS description
    FROM sections
    WHERE sections.section_id = (SELECT section_id FROM section_names WHERE section_name = '{section_name}'); -- название, описание товара по названию раздела
  """)
  f = cursor.fetchall()
  conn.close()
  return f


def get_section_from_id(id): # 1 2 3
  conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
  cursor = conn.cursor()
  cursor.execute(f"""
  SELECT 
    section_name AS 'Название раздела' FROM section_names 
    WHERE section_id = (SELECT section_id FROM sections WHERE product_id = {id})
  """)
  f = cursor.fetchone()
  conn.close()
  return f


def get_max_min():
  conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
  cursor = conn.cursor()
  cursor.execute("""
  SELECT 
    product_name, max(price) FROM product_info
  UNION 
  SELECT
  product_name, min(price) FROM product_info;
  """)
  f = cursor.fetchall()
  conn.close()
  return f


def join_info_id():
  conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
  cursor = conn.cursor()
  cursor.execute("""
  SELECT * 
    FROM product_info JOIN sections
    ON product_info.product_id = sections.product_id; -- объединение описания товара и id его секции
  """)
  f = cursor.fetchall()
  conn.close()
  return f


print(get_name_from_id(1))
#print(get_name_from_section('Другое'))
#print(get_section_from_id(1))
#print(get_max_min())
#print(join_info_id())
