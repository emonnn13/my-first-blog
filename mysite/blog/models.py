from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    #Sets the time using current timezone when created
    created_date = models.DateTimeField(default=timezone.now)
    #It can be blank, as not published yet
    published_date = models.DateTimeField(blank=True, null=True)

    #Updates the published_date if it is published
    def publish(self):

        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title