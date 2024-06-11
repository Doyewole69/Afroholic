from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
class upcomingproject1(models.Model):
    artist_name = models.CharField(max_length=15, blank=False)
    song_name = models.CharField(max_length=25, blank=False)
    project_image = models.ImageField(upload_to = 'static/images/project/')
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.artist_name
    
class upcomingproject2(models.Model):
    artist_name = models.CharField(max_length=15, blank=False)
    song_name = models.CharField(max_length=25, blank=False)
    project_image = models.ImageField(upload_to = 'static/images/project/')
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.artist_name
    
    
class merch1(models.Model):
    merch_name = models.CharField(max_length=25)
    merch_image = models.ImageField(upload_to = 'static/images/merch/')
    merch_description = models.TextField()
    merch_price = models.IntegerField()
    merch_link = models.URLField(max_length=200)

    def __str__(self):
        return self.merch_name
    
    
class merch2(models.Model):
    merch_name = models.CharField(max_length=25)
    merch_image = models.ImageField(upload_to = 'static/images/merch/')
    merch_description = models.TextField()
    merch_price = models.IntegerField()
    merch_link = models.URLField(max_length=200)

    def __str__(self):
        return self.merch_name
    
    
class news(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = 'static/images/news/')
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title