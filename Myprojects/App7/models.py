from django.db import models

# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Courses(models.Model):
    name=models.CharField(max_length=50)
    discription=models.TextField()
    Students=models.ManyToManyField(Students,related_name='courses',blank=True)
    
    def __str__(self):
        return self.name