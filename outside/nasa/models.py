from django.db import models

# Create your models here

class Media(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=1024)
  description = models.CharField(max_length=1024)
  url = models.CharField(max_length=1024)
  media_type = models.CharField(max_length=32)
  extra_info = models.CharField(max_length=1024)

  class Meta:
    indexes = [
      models.Index(fields=['date']),
    ]

  def __str__(self):
    return self.title