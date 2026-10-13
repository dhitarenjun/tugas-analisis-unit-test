import unittest
from main import hitung_diskon, cek_status, login_user

class TestAplikasi(unittest.TestCase):
    def test_diskon(self):
        self.assertEqual(hitung_diskon(120000), 108000.0)
        self.assertEqual(hitung_diskon(50000), 50000)

    def test_status(self):
        self.assertEqual(cek_status(75), "Member VIP")
        self.assertEqual(cek_status(10), "Member Reguler")

    def test_login(self):
        self.assertTrue(login_user("ardhita"))
        self.assertFalse(login_user("salah"))

if __name__ == '__main__':
    unittest.main()