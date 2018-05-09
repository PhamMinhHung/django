from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# Create your models here.
# mvc model

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True,blank=True)
    content = models.TextField(null=True)
    author = models.TextField(null=True)
    date =models.DateTimeField(auto_now_add=True)
    # def __unicode__(self):
    #     return self.title
    # def __str__(self):
    #     return self.title
    # def get_absolute(self):
    #     return reverse("posts:detail", kwargs={"id" : self.id})
    #
    # class Meta:
    #     ordering=["-timestamp","updated"]