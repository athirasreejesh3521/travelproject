from django.db import models

# Create your models here.
class official(models.Model):
    name= models.CharField(max_length=250)
    image =models.ImageField(upload_to='photo')
    Position=models.TextField()

    def __str__(self):
        return self.name
