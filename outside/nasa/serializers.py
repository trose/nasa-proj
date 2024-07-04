from rest_framework import serializers
from .models import Media
class MediaSerializer(serializers.ModelSerializer):
  def create(self):
    return Media.objects.create(
      title=self.data['title'],
      description=self.data.get('description', ''),
      date=self.data['date'],
      url=self.data['url'],
      media_type=self.data['media_type'],
      extra_info=self.data['extra_info'],
    )

  class Meta:
    model = Media
    fields = ['date', 'title', 'description', 'url', 'media_type', 'extra_info']
