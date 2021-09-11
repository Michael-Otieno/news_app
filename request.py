from app import app
import urllib.request, json
from app.models.source import Source

Source = Source

#Getting apiKey
api_key = app.config['SOURCE_API_KEY']

#Getting the news base url
base_url = app.config['SOURCE_API_BASE_URL']

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
        # id = source_item('id')
        name = source_item.get('name')
        title = source_item.get('title')
        description = source_item.get('description')
        category = source_item.get('category')
        # language = source_item('language')

        source_object = Source( name, title, description, category)
        source_results.append(source_object)

    return source_results