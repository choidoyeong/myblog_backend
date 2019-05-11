from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    category_name = models.CharField(max_length = 200)
    post_count = models.IntegerField(default=0)

class Post(TimeStampedModel):
    post_title = models.CharField(max_length = 200)
    post_content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,)
    like = models.IntegerField(default=0)

class Opinion(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    opinion_content = models.TextField()
    post_content = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Comment(TimeStampedModel):
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    comment_content = models.TextField()
    from_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='from_user')
    to_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='to_user')