import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("please"),
        "s'il vous plaît")
        self.assertEqual(englishToFrench("sorry"),"Pardon")
        self.assertNotEqual(englishToFrench("pardon me"),
        "pardon me")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("s'il vous plaît"),
        "please")
        self.assertEqual(frenchToEnglish("Pardon"),"sorry")
        self.assertNotEqual(frenchToEnglish("droit"),"droit")

class TestNull_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(frenchToEnglish(None))

class TestNull_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNone(englishToFrench(None))

class TestHello(unittest.TestCase):
    def test2(self):
        self.assertEqual(englishToFrench("hello"),"Bonjour")

class TestBonjour(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"hello")

unittest.main()
