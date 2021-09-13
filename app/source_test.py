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
        self.new_source = Source('id',"name","title","description", "category","image",'url')########

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
        self.new_article = Article("id","name","title", "description", "url", "image",'publishedAt',"content")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()