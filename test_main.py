import unittest
from main import tinh_diem_gpa
class TestTinhDiemGPA(unittest.TestCase):
    def test_tinh_diem_gpa(self):
        self.assertEqual(tinh_diem_gpa(8.5), 4.0)
        self.assertEqual(tinh_diem_gpa(7.0), 2.8)
        self.assertEqual(tinh_diem_gpa(9.0), 4.0)
        self.assertEqual(tinh_diem_gpa(6.5), 2.6)   
if __name__ == '__main__':
    unittest.main()