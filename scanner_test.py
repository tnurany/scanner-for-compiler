import unittest
from scanner import scan

class ScannerTest(unittest.TestCase):
  
    # Returns True or False. 
    def test_1(self):        
        self.assertEqual(scan("a"),"Accept")

    def test_2(self):
        self.assertEqual(scan("abacxy"),"Accept")

    def test_3(self):
        self.assertEqual(scan("CamelCaseNaMe"),"Accept")

    def test_4(self):
        self.assertEqual(scan("CamelCaseWith123abc"),"Accept")

    def test_5(self):
        self.assertEqual(scan("a2B37qrv90"),"Accept")

    def test_6(self):
        self.assertEqual(scan("12"),"Reject")

    def test_7(self):
        self.assertEqual(scan("1abc"),"Reject")

    def test_8(self):
        self.assertEqual(scan(""),"Reject")

    def test_9(self):
        self.assertEqual(scan("ab_"),"Reject")

if __name__ == '__main__':
    unittest.main()