import requests
import os
from dotenv import load_dotenv
from Answer import Answer

load_dotenv()
API_KEY = os.getenv('API_KEY')
CSE = os.getenv('CSE')

class CustomSearch:

  @staticmethod
  def get_answers (search):
    answers = []
    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE}&cr=countryBR&gl=br&lr=lang_pt&q={search}'

    data = requests.get(url).json()
    search_items = data.get('items')
    
    for i, search_item in enumerate(search_items, start=1):
      print(search_item)
      answer = Answer(search_item.get('title'), search_item.get('link'), search_item.get('displayLink'), search_item.get('snippet'))

      answers.append(answer)
    
    return answers

    


