from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # Stores a short label that helps organize discoveries.
    name = models.CharField(max_length=100)

    def __str__(self):
        # Shows the category name instead of a confusing object label.
        return self.name


class Discovery(models.Model):
    # Stores the main name of the trail discovery.
    title = models.CharField(max_length=150)

    # Stores where the discovery happened.
    location = models.CharField(max_length=150)

    # Stores the date the user saw or recorded the discovery.
    date_seen = models.DateField()

    # Stores the user's longer notes about what they noticed.
    description = models.TextField()

    # Stores a short safety reminder for people exploring the desert.
    safety_tip = models.CharField(max_length=255)

    # Stores a short reminder that helps protect nature and wildlife.
    preservation_tip = models.CharField(max_length=255)

    # Stores an optional image link without forcing users to upload a file.
    image_url = models.URLField(blank=True)

    # Connects each discovery to one category, like Animal or Rock Formation.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Connects each discovery to the user who created it.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Saves the time this discovery was first created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows the discovery title in admin and debugging tools.
        return self.title
    
    