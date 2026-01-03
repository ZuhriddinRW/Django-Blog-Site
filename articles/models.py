from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import BaseModel


class Article ( models.Model, BaseModel ) :
    title = models.CharField ( max_length=150 )
    summary = models.CharField ( max_length=50, blank=True, null=True )
    body = models.TextField ()
    photo = models.ImageField ( upload_to='images/', blank=True )
    author = models.ForeignKey (
        get_user_model (),
        on_delete=models.CASCADE
    )

    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        return reverse ( 'article_detail', args=[str ( self.id )] )