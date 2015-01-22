from django.db import models


class Contact(models.Model):

    first_name = models.CharField(max_length=255, blank=False,)
    last_name = models.CharField(max_length=255, blank=True,)
    email = models.EmailField(max_length=254, blank=True,)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
