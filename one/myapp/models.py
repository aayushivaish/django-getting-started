from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class short_url(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    short_url = models.CharField(max_length = 20)
    long_url = models.URLField("URL" , unique = True)
    def __str__(self):
        return self.user.username
# Create your models here.
class websites(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    long_url = models.URLField("URL" , unique = True)
    def __str__(self):
        return self.long_url
