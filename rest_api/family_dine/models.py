from django.db import models


class Dine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.ForeignKey('DineLocation', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('auth.User', related_name='dine_opened', on_delete=models.CASCADE)
    participant = models.ManyToManyField('auth.User', related_name='dine_joined', blank=True)

    def __str__(self):
        return self.name


class DineLocation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


