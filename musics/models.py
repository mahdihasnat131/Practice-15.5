from django.db import models

# Create your models here.
class Music(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField()
    phone_no=models.CharField(max_length=12)
    instrument_type=models.TextField()

    def __str__(self):
        return self.first_name
