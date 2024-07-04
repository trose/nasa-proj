import requests

class NasaClient():
  """
  Client for interacting with NASA APOD API
  """
  API_KEY = '8yvDlHPytPFR7eVhvTQmpf0zYbW1naG51EtJMr23'
  url = 'https://api.nasa.gov/planetary/apod'

  def get_by_date(self, date):
    resp = requests.get(self.url, params={
      'date': date,
      'api_key': self.API_KEY
    })
    return resp.json()

class WikiClient():
  """
  Client for interacting with wikipedia OpenSearch
  """
  url = 'https://en.wikipedia.org/w/api.php'

  def search(self, term):
    params = {
        'action': 'opensearch',
        'search': term,
        'limit': '1',
        'profile': 'normal',
        'format': 'json'
    }

    resp = requests.get(self.url, params=params)
    return resp.json()