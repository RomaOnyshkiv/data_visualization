from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)
    year = models.CharField(max_length=20)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class Languages(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language
