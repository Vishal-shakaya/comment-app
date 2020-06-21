from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    comments = GenericRelation(Comment)

    def get_absolute_url(self):
    	return reverse('Post_app:detail' , kwargs={'pk': self.pk})
# Create your models here.
