from django.db import models

class Game(models.Model):
    titulo = models.CharField(max_length=255)
    plataformas = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

