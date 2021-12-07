from sqlrequest import *
import unittest
conn = sqlite3.connect('F:/HWlog/NOTNOW.db')
cursor = conn.cursor()

class TestSqlrequest(unittest.TestCase):
    def test_get_name_from_id(self):
        self.assertEqual(get_name_from_id(1),(1, 'Видеокарта RTX 3060Ti', 'ритейл $400, но ты все равно купишь'), 'Must be RTX3060')

    def test_get_name_from_section(self):
        self.assertEqual(get_name_from_section('Другое'),[('Овсяный порридж с малиной', 'Овсяный эко-порридж с малиновыми беррис, выращенными на хоум плентспейс')],'Must be porrige')
    
    def test_get_section_from_id(self):
        self.assertEqual(get_section_from_id(1),('Электроника',), 'Must be Электроника')
    
    def test_get_max_min(self):
        self.assertEqual(get_max_min(),[('Видеокарта RTX 3060Ti', 1048.0), ('Овсяный порридж с малиной', 500.0)],'Must be rtx-porrige')

    def test_join_info_id(self):
        self.assertEqual(join_info_id(), [(1, 'Видеокарта RTX 3060Ti', 1048.0, 'ритейл $400, но ты все равно купишь', 0, '2021-11-15', '', 1, 1), (2, 'Видеокарта Palit GTX 1050Ti', 843.0, 'убийца рейтрейсинга и dlss, да еще и Palit…', 3, '2021-11-27', None, 2, 1), (3, 'Овсяный порридж с малиной', 500.0, 'Овсяный эко-порридж с малиновыми беррис, выращенными на хоум плентспейс', 99, '2021-10-20', None, 3, 2)] ,'Must print all')
    
        

if __name__ == '__main__':
    unittest.main()   
cursor.close()