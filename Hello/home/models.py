from django.db import models

# Create your models here.

#pyhton manage.py makemigrations ------create changes and store in a file
#pyhton manage.py migrate ----apply the pending chanegs created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=122)
    description =models.TextField()
    date = models.DateField()

    def __str__(self):
       return self.name
   

