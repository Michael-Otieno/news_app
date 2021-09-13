class Source:
    '''
    Source class to define Source objects
    '''
    def __init__(self,id, name,title, description,category, urlToImage,url):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.category = category
        self.image = urlToImage
        self.url = url


class Article:
    '''
    Article class to define Articles objects
    '''
    def __init__(self,id, name, title,description,url,urlToImage,publishedAt, content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.image = urlToImage
        self.publishedAt = publishedAt
        self.content = content


