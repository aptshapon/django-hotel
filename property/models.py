from django.db import models


# choices
property_type = (
    ('sale', 'sale'),
    ('rent', 'rent'),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    beds_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property', null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.name