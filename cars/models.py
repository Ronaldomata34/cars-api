from django.db import models


class Car(models.Model):
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE, related_name="cars_model")
    color = models.CharField(max_length=55)
    price = models.IntegerField()

    def __str__(self):
        return self.model.make + self.model.name

class CarMake(models.Model):
    key = models.CharField(max_length=25)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=55)
    make = models.ForeignKey('CarMake', on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return self.name