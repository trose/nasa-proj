import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from .models import Media
# Create your tests here.

class TestViews(APITestCase):
  def setUp(self):
    return super().setUp()
    
  @patch('nasa.clients.WikiClient.search', autospec=True)
  @patch('nasa.clients.NasaClient.get_by_date', autospec=True)
  def test_APOD_GET_happy_path(self, MockNasaClient, MockWikiClient):
    MockWikiClient.return_value = [[],[],[],[]]
    MockNasaClient.return_value = {
      'title': 'something',
      'explanation': 'something',
      'media_type': 'image',
      'date': '2024-06-03',
      'url': 'something'
    }

    resp = self.client.get('/nasa/apod', {'date': '2024-06-03'})
    
    self.assertEqual(resp.status_code, status.HTTP_200_OK)
    assert MockNasaClient.called
    assert MockWikiClient.called

  @patch('nasa.clients.WikiClient.search', autospec=True)
  @patch('nasa.clients.NasaClient.get_by_date', autospec=True)
  def test_APOD_GET_cached_happy_path(self, MockNasaClient, MockWikiClient):
    media = Media.objects.create(
      title='Time Spiral',
      description='What\'s happened since the universe started?',
      date='2024-07-03',
      url='https://apod.nasa.gov/apod/image/2407/TimeSpiral_Budassi_960.jpg',
      media_type='image',
      extra_info=''
    )
    resp = self.client.get('/nasa/apod', {'date': '2024-07-03'})
    
    self.assertEqual(resp.status_code, status.HTTP_200_OK)
    MockNasaClient.assert_not_called
    MockWikiClient.assert_not_called

  def test_APOD_GET_future_err(self):
    resp = self.client.get('/nasa/apod', {'date': datetime.date.today() + datetime.timedelta(days=1) })
    
    self.assertEqual(resp.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

  def test_APOD_GET_before_start_err(self):
    resp = self.client.get('/nasa/apod', {'date': datetime.date(1995, 6, 1) })
    
    self.assertEqual(resp.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)