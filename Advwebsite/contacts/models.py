from django.db import models

# Create your models here.
class Contacts(models.Model):
    listing_title= models.CharField(max_length=200)
    listing_id = models.IntegerField()
    user_id=models.IntegerField(blank='True')
    name=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank='True')
    message = models.TextField(blank='True')

    def __str__(self):
        return self.name