from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Like(models.Model):
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Posts(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class LikeDislike(models.Model):
    like = models.BooleanField()
    dislike = models.BooleanField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self


class Comments(models.Model):
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, )

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-created']