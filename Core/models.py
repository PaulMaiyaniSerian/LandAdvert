from django.db import models

# Create your models here.
class Property(models.Model):
    pic = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    Location = models.CharField(max_length=255)
    latest = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sold = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    
    
class Land(Property):

    def __str__(self):
        return self.name

class Ranch(Property):
    
    def __str__(self):
        return self.name


class OtherProperty(Property): 
        
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name