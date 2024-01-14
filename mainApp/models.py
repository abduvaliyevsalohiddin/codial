from django.db import models


class Soha(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Savollar(models.Model):
    nom = models.CharField(max_length=30)
    variat = models.PositiveSmallIntegerField()
    soha = models.ForeignKey(Soha, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
