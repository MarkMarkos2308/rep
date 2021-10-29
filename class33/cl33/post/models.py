from django.db import models


class post(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title} |            {self.description}'
