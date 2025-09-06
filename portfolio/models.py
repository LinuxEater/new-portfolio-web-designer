from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    TYPE_CHOICES = [
        ('fullstack', 'fullstack'),
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('mobile', 'mobile'),
        ('scraping', 'scraping'),
        ('bots', 'bots'),
        ('data-analysis', 'data-analysis'),
        ('cybersecurity', 'cybersecurity'),
        ]
    
    
    title = models.CharField(max_length=200)
    short_description = RichTextField()
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    technologies = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=TYPE_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='projects/')
    url_github = models.CharField(blank=True, null=True, max_length=255)
    url_blog_project = models.CharField(blank=True, null=True, max_length=255)
    url_demo_live = models.CharField(blank=True, null=True, max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

