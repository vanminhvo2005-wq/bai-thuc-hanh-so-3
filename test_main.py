import unittest
from main import tinh_dim_gpa
class TestTinhDimGPA(unittest.TestCase):
    def test_tinh_dim_gpa(self):
        self.assertEqual(tinh_dim_gpa(8.5), 4.0)
        self.assertEqual(tinh_dim_gpa(7.0), 2.8)
        self.assertEqual(tinh_dim_gpa(9.0), 4.0)
        self.assertEqual(tinh_dim_gpa(6.5), 2.6)
if __name__ == '__main__':
    unittest.main()