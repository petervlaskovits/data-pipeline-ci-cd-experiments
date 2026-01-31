import unittest
import pandas as pd

from transformations import clean_column

class TestCleaning(unittest.TestCase):
    test_column_1 = pd.Series([
        "$10/hr",
        "$15 per hour",
        "$12/hr"
    ])

    def test_column_cleaning_salaries(self):
        result = clean_column(self.test_column_1)
        salaries = result.iloc[:, 1]
        self.assertTrue(salaries.equals(pd.Series([10, 15, 12])))

    def test_column_cleaning_currency(self):
        result = clean_column(self.test_column_1)
        currency = result.iloc[:, 2]
        self.assertTrue(
            currency.equals(pd.Series([
                        "USD",
                        "USD", 
                        "USD"
                    ]
                )
            )
        )

    def test_column_cleaning_salary_info(self):
        result = clean_column(self.test_column_1)
        salary_infos = result.iloc[:, 3]
        self.assertTrue(salary_infos.equals(pd.Series([
                    "Hourly",
                    "Hourly",
                    "Hourly"
                ])
            )
        )

if __name__ == "__main__":
    unittest.main()
        