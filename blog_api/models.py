from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Use RichTextField here
    published_date = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    email = models.EmailField(unique=True)  # Email must be unique
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Automatically set the subscription date

    def __str__(self):
        return self.email