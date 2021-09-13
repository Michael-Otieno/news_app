import unittest
from app.models.source import Source, Article######

Source = Source
Article = Article####

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source('id',"TechCrunch","Fitbit adds ECG and stress-level",
        "Fitness band market", "share is undoubtedly contracting","category")########

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

##Added testcase
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article("id","TechCrunch","Fitbit adds ECG and stress-level",
        "Fitness band", "market share is", "undoubtedly contracting",'publishedAt',"category")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()