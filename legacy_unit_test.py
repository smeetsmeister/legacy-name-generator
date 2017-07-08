import unittest
import legacy_name_generator

class LegacyUnitTests(unittest.TestCase):
    def testGetRandomWords(self):
        expected = 5
        result = len(legacy_name_generator.getRandomWords(expected))
        self.assertEqual(result, expected)