from django.db import models
from tinymce.models import HTMLField

# Create your models here.

TITLE_CHOICES = [
    ('Django', 'Django'),
    ('Html', 'HTML'),
    ('CSS', 'CSS'),
    ('JS', 'JS'),
    ('Python', 'Python'),
    ('Android', 'Android')
]
class CreateBlog(models.Model):
    cat = models.CharField(max_length=7, choices=TITLE_CHOICES, default='Djnago')
    title = models.CharField(max_length = 20)
    slug = models.SlugField(max_length = 250, null=False, unique=True)
    short_des = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    content = HTMLField('Content')

    def __str__(self):
        return self.title
    
