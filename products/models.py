from django.db import models

# Create your models here.
class products(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    description=models.TextField(blank=True,default='')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    objects= models.Manager()
    
    def __str__(self):
        return self.name


