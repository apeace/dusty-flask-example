import unittest

class TestTrivialPythonStuff(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_downer(self):
        self.assertEqual('FOO'.lower(), 'foo')

if __name__ == '__main__':
    unittest.main()
