from django.db import models
 # Import ResourcesForm from forms.py in the same directory


class Resources(models.Model):
    booktitle = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    bookcover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.booktitle
