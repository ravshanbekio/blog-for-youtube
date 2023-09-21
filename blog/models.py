from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=400)
    #image = models.ImageField()

    def __str__(self):
        return self.title