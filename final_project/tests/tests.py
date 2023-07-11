import unittest
from machinetranslation import translator

class TestF2E(unittest.TestCase):
    """test translation to English"""
    def test1(self):
        """confirms bonjour=>hello"""
        self.assertEqual(translator.french_to_english('bonjour'), 'hello')
    def test2(self):
        """confirms c'est la vie=>it's the world"""
        self.assertEqual(translator.french_to_english('c\'est la vie'), 'it\'s the world')

class TestE2F(unittest.TestCase):
    """tests translation to French"""
    def test1(self):
        """confirms hello=>bonjour"""
        self.assertEqual(translator.english_to_french('hello'), 'bonjour')
    def test2(self):
        """confirms it's the world=>c'est la vie"""
        self.assertEqual(translator.english_to_french('it\'s the world'), 'c\'est la vie')

unittest.main()
