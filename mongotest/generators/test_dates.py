import unittest
import re
import random

import dates
from .. import consistency_checks

class TestDateGenerator(unittest.TestCase, consistency_checks.ConsistencyChecker):
    def test_date_generation(self):
        for _ in xrange(1000):
            sample_date = dates.random_datetime()

            iso_match = re.match("(?P<year>[0-9]{4})-(?P<month>[01][0-9])-(?P<day>[0-3][0-9])T(?P<hour>[0-2][0-9]):(?P<minute>[0-5][0-9]):(?P<second>[0-5][0-9])", sample_date['iso'])

            self.assertIsNot(iso_match, None)

            year = int(iso_match.group('year'))
            month = int(iso_match.group('month'))
            day = int(iso_match.group('day'))
            hour = int(iso_match.group('hour'))
            minute = int(iso_match.group('minute'))
            second = int(iso_match.group('second'))

            self.assertEqual(year, sample_date['date']['year'])
            self.assertEqual(month, sample_date['date']['month'])
            self.assertEqual(day, sample_date['date']['day'])
            self.assertEqual(hour, sample_date['date']['hour'])
            self.assertEqual(minute, sample_date['date']['minute'])
            self.assertEqual(second, sample_date['date']['second'])

            days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            self.assertGreaterEqual(year, 1970)
            self.assertLessEqual(year, 2100)
            self.assertGreaterEqual(month, 1)
            self.assertLessEqual(month, 12)
            self.assertGreaterEqual(day, 1)
            self.assertLessEqual(day, days_per_month[month - 1])
            self.assertGreaterEqual(hour, 0)
            self.assertLessEqual(hour, 23)
            self.assertGreaterEqual(minute, 0)
            self.assertLessEqual(minute, 59)
            self.assertGreaterEqual(second, 0)
            self.assertLessEqual(second, 59)

    def test_date_consistency(self):
        self.check_consistency(dates.random_datetime)
      
