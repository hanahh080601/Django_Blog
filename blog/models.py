from django.db import models
from django.conf import settings
from django.utils import timezone

#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
    #this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #define text with a limited number of characters.
    title = models.CharField(max_length=200)

    #this is for long text without a limit
    text = models.TextField()

    #date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
