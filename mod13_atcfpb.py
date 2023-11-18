import unittest
from datetime import datetime

class TestInputs(unittest.TestCase):

    def test_symbol(self):
        # Test capitalized 1-7 alpha character input
        self.assertTrue(self.validate_symbol("GOOGL"))  
        self.assertFalse(self.validate_symbol("googl"))
        self.assertFalse(self.validate_symbol("GOOGLES"))
        self.assertFalse(self.validate_symbol("123"))

    def test_chart_type(self):
        # Test 1 numeric character, 1 or 2
        self.assertTrue(self.validate_chart_type("1"))
        self.assertTrue(self.validate_chart_type("2"))
        self.assertFalse(self.validate_chart_type("3"))
        self.assertFalse(self.validate_chart_type("12"))

    def test_time_series(self):
        # Test 1 numeric character, 1-4  
        self.assertTrue(self.validate_time_series("1"))
        self.assertTrue(self.validate_time_series("2"))
        self.assertTrue(self.validate_time_series("3"))
        self.assertTrue(self.validate_time_series("4"))
        self.assertFalse(self.validate_time_series("5"))

    def test_start_date(self):
        # Test date format YYYY-MM-DD
        self.assertTrue(self.validate_date("2022-01-01"))
        self.assertFalse(self.validate_date("01-01-2022"))
        self.assertFalse(self.validate_date("20220101"))

    def test_end_date(self):
        # Test date format YYYY-MM-DD
        self.assertTrue(self.validate_date("2022-12-31"))
        self.assertFalse(self.validate_date("31-12-2022"))
        self.assertFalse(self.validate_date("20221231"))

    def validate_symbol(self, symbol):
        return symbol.isalpha() and symbol.isupper() and 1<=len(symbol)<=7

    def validate_chart_type(self, chart_type):
        return chart_type in ["1", "2"]

    def validate_time_series(self, time_series):
        return time_series in ["1","2","3","4"] 
    
    def validate_date(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    unittest.main()