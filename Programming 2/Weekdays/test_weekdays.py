import unittest
from datetime import date
from weekdays import weekdays


class TestWeekdays(unittest.TestCase):
    """Implement tests for weekdays here."""

    def test_one_day(self):
        self.assertEqual(weekdays(date(2022, 1, 19), date(2022, 1, 20)), 16)

    def test_full_week(self):
        self.assertEqual(weekdays(date(2022, 2, 5), date(2022, 2, 13)), 40)


if __name__ == "__main__":
    unittest.main()
