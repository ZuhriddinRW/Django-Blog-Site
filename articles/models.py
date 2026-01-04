from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article ( models.Model ) :
    title = models.CharField ( max_length=150 )
    summary = models.CharField ( max_length=50, blank=True )
    body = RichTextUploadingField()
    photo = models.ImageField ( upload_to='images/', blank=True )
    author = models.ForeignKey (
        get_user_model (),
        on_delete=models.CASCADE
    )

    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        return reverse ( 'article_detail', args=[str ( self.id )] )

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # TextField allows users to write normal-length comments from the article page.
    # The max_length is enforced at the form/validation layer.
    comment = models.TextField(max_length=800)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.article_id)])