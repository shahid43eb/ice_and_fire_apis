from json import loads

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    isbn = models.CharField(max_length=50)
    authors = models.CharField(max_length=1000)
    number_of_pages = models.PositiveIntegerField(default=0)
    publisher = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    release_date = models.DateTimeField()

    def __str__(self):
        return '{} By {}'.format(self.name, ",".join(self.get_authors()))

    def get_authors(self):
        return loads(self.authors.replace("'", '"'))
