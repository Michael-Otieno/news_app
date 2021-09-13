from app import app
import urllib.request, json
# from app.models import source
from app.models.source import Source, Article

Source = Source
Article = Article


#Getting apiKey
api_key = app.config['SOURCE_API_KEY']

#Getting the news base url
base_url = app.config['SOURCE_API_BASE_URL']
article_url = app.config['ARTICLE_API_BASE_URL']



def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Functio that processes the news results and transforms them to a list of objects
    Args:
        news_list: list of dictionaries that contain movie details
    Return:
        news_results: list of news objects
    '''

    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        title = source_item.get('title')
        description = source_item.get('description')
        category = source_item.get('category')
        image = source_item.get('urlToImage')
        url = source_item.get('url')

        source_object = Source( name, title, description, category,image, url)
        source_results.append(source_object)

    return source_results


############################
def get_articles(id):
    '''
    Function that gas the json response to our url request
    '''
    get_articles_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            article_results = process_results[articles_results_list]

    return article_results

def process_article_results(article_list):
    '''
    Function that processes the articles results and transforms them to a list of objects
    Args:
       article_list: A list of dictionaries that contains articles details
    Return:
        article_results: a list of article objects 
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')


        article_object = Article(id,name,title,description, url,image,publishedAt,content)
        article_results.append(article_object)

    return article_results

