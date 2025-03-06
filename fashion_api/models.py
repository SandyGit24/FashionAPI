from django.db import models

class FashionItem(models.Model):
    PET_CATEGORIES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('Rabit', 'Rabit'),

    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pet_category = models.CharField(max_length=50, choices=PET_CATEGORIES)
    image_url = models.URLField()

    def __str__(self):
        return self.name
