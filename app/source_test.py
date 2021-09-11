import unittest
from models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source("TechCrunch","Fitbit adds ECG and stress-level",
        "Fitness band market share is undoubtedly contracting","category")########

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
    unittest.main()