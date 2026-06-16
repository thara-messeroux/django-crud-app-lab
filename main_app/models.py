from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # Stores one main label that organizes each discovery.
    name = models.CharField(max_length=100)

    class Meta:
        # Shows the correct plural name in Django admin.
        verbose_name_plural = 'Categories'

    def __str__(self):
        # Shows the category name instead of a confusing object label.
        return self.name


class Tag(models.Model):
    # Stores flexible reusable labels like scenic, safety, wildlife, or sunset.
    name = models.CharField(max_length=50)

    class Meta:
        # Keeps tags ordered and readable in admin.
        ordering = ['name']

    def __str__(self):
        # Shows the tag name clearly in forms and admin.
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

    # Stores an optional uploaded image from the user's computer.
    image_upload = models.ImageField(upload_to='discovery_images/', blank=True, null=True)

    # One category can organize many discoveries.
    # PROTECT prevents deleting a category if discoveries still use it.
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    # Many discoveries can share many tags.
    # Example: scenic, wildlife, safety, sunset.
    tags = models.ManyToManyField(Tag, blank=True)

    # Connects each discovery to the user who created it.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Saves the time this discovery was first created.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Shows the correct plural name in Django admin.
        verbose_name_plural = 'Discoveries'

    def __str__(self):
        # Shows the discovery title in admin and debugging tools.
        return self.title
