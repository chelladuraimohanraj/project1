from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    rate=models.IntegerField()
    image=models.ImageField(upload_to='uploads',null=True)
    
    def __str__(self):
        return self.name
