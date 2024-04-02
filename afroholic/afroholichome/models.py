from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
class project(models.Model):
    project_image = models.ImageField(upload_to = 'static/images/project/ ')
    artist_name = models.CharField(max_length=25, blank=False)
    work_name = models.CharField(max_length=25, blank=False)
    
    def __str__(self):
        return self.artist_name