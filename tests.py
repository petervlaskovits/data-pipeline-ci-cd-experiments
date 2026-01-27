import unittest

from main import clean_column

class TestCleaning(unittest.TestCase):
    test_column_1 = [
            "$10/hr",
            "$15 per hour",
            "$12/hr"
    ]

    def test_column_cleaning_salaries(self):
        result = clean_column(self.test_column_1)
        salaries = result[0]
        self.assertEqual(salaries, [
            10,
            15,
            12
        ])

    def test_column_cleaning_currency(self):
        result = clean_column(self.test_column_1)
        currency = result[1]
        self.assertEqual(currency, [
            "USD",
            "USD",
            "USD"
        ])

    def test_column_cleaning_salary_info(self):
        result = clean_column(self.test_column_1)
        salary_infos = result[2]
        self.assertEqual(salary_infos, [
            "hourly",
            "hourly",
            "hourly"
        ])

if __name__ == "__main__":
    unittest.main()
        