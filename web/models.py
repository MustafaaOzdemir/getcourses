from django.db import models



# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Course(models.Model):
    """Model representing a course (but not a specific copy of a course)."""
    title = models.CharField(max_length=200)
    image = models.TextField(max_length=500)
    video = models.TextField(max_length=500)

    description= models.TextField(max_length=1000, help_text='Enter a brief description of the course')
     
    #teacher = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this course."""
        return reverse('course-detail', args=[str(self.id)])    


class Category (models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, default=0.0, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this course."""
        return reverse('course-detail', args=[str(self.id)])  
#from django.db import models




