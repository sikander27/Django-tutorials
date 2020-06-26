from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=30)
    ename = models.CharField(max_length=30)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

    def __str__(self):
        return self.first_name

class Company(models.Model):
    name=models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date_created = models.DateField()

    def __str__(self):
        return self.name
        
class Language(models.Model):
    name=models.CharField(max_length=20)
    creator = models.CharField(max_length=30)
    paradigm = models.CharField(max_length=30)
    date_created = models.DateField()
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name=models.CharField(max_length=30)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name

#Profile page Extending existing user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
