from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    image=models.FilePathField(path="portfolio/static/img")

    def __str__(self):
        return self.title
    