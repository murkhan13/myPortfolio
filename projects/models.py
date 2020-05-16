from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img", default="project1.png")

    def __str__(self):
        return self.title
    
    def get_image_url(self, obj):
        return obj.image.url

    
