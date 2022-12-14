from unittest.case import TestCase
from main import geo_logs_sort

class TestMain(TestCase):
    def test_geo_logs(self):
        res = geo_logs_sort()
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], dict)
        self.assertEqual(len(res), 6)
        
        for x in res[0].values():
            self.assertEqual('Россия', x[1])
        