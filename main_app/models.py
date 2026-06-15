from django.db import models


class Category(models.Model):
    # Stores a short category name, like Animal, Plant, or Rock Formation.
    name = models.CharField(max_length=100)

    def __str__(self):
        # Shows the category name in Django admin and debugging tools.
        return self.name
