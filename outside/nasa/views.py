import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .clients import NasaClient, WikiClient
from .models import Media
from .serializers import MediaSerializer

# Create your views here.

class MediaView(APIView):
  start_date = datetime.date(1995, 6, 16)
  end_date = datetime.date.today()

  def get(self, request, *args, **kwargs):
    date = request.GET.get('date')
    if not date:
      return Response('date parameter is required.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if (datetime.date.fromisoformat(date) < self.start_date or
        datetime.date.fromisoformat(date) > self.end_date):
      return Response('Date must be between Jun 16, 1995 and Today.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # check if we have media cached
    media = Media.objects.filter(date=date)

    if len(media):
      serializer = MediaSerializer(media[0])
      return Response(serializer.data)

    nasa_media = NasaClient().get_by_date(date=date)
    nasa_media['description'] = nasa_media.get('explanation', '')

    # extra data from wikipedia

    wikiSearch = WikiClient().search(nasa_media['title'])

    nasa_media['extra_info'] = {
      'source': 'Wikipedia',
      'url': wikiSearch[3][0]
    } if len(wikiSearch[3]) else {}

    # save
    serializer = MediaSerializer(nasa_media)
    serializer.create()

    return Response(serializer.data)