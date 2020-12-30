import json

from django.db import models
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse


class Category(models.Model):
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Posts(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    # def like_or_dislike_func(self, request, post):
    #     try:
    #         post = Posts.objects.get(pk=pk)
    #     except:
    #         raise Http404("Пост не найден!")
    #     old_like = LikeDislike.objects.filter(user=request.user, post=post)
    #     if old_like:
    #         like = LikeDislike.objects.get(user=request.user, post=post)
    #         print(like, is_like)
    #         if like.like_or_dislike == 'like' and is_like == 'like':
    #             like.delete()
    #             post.like -= 1
    #             post.save()
    #         elif like.like_or_dislike == 'dislike' and is_like == 'dislike':
    #             like.delete()
    #             post.dislike -= 1
    #             post.save()
    #         elif like.like_or_dislike == 'like' and is_like == 'dislike':
    #             like.like_or_dislike = 'dislike'
    #             like.save()
    #             post.dislike += 1
    #             post.like -= 1
    #             post.save()
    #         elif like.like_or_dislike == 'dislike' and is_like == 'like':
    #             like.like_or_dislike = "like"
    #             like.save()
    #             post.dislike -= 1
    #             post.like += 1
    #             post.save()
    #     else:
    #     new_like = LikeDislike(user=request.user, post=post, like_or_dislike='like')
    #     new_like.save()
    #     if is_like == 'like':
    #     elif is_like == 'dislike':
    #         self.dislike += 1
    #         post.save()
    #
    #     is_like = LikeDislike.objects.filter(user=request.user, post=post)
    #     if is_like:
    #         user_like = True
    #         is_like = LikeDislike.objects.get(user=request.user, post=post)
    #         user_like_val = is_like.like_or_dislike
    #     else:
    #         user_like = False
    #         user_like_val = ''
    #
    #     return self.add_like()

    def add_like(self, request, post):
        old_like = LikeDislike.objects.filter(user=request.user, post=post)
        if old_like:
            like = LikeDislike.objects.get(user=request.user, post=post)
            print("Вы уже оценивали эту запись")
        else:
            self.like += 1
            self.save()
            new_like = LikeDislike(user=request.user, post=post, like_or_dislike='like')
            new_like.save()
        return self.like

    def add_dislike(self, request, post):
        old_dislike = LikeDislike.objects.filter(user=request.user, post=post)
        if old_dislike:
            dislike = LikeDislike.objects.get(user=request.user, post=post)
            print("Вы уже оценивали эту запись")
        else:
            self.dislike += 1
            self.save()
            new_dislike = LikeDislike(user=request.user, post=post, like_or_dislike='like')
            new_dislike.save()
        return self.dislike

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class LikeDislike(models.Model):
    like_or_dislike_choice = (
        ("Like", "like"),
        ('Dislike', 'dislike'),
        (None, 'None')
    )
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_or_dislike = models.CharField(max_length=10, choices=like_or_dislike_choice, default=None, null=True)


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


class Statistics(models.Model):
    like_stat = models.IntegerField(default=0)
    dislike_stat = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculate_stat(self, request,):
        posts = Posts.objects.all()
        if posts:
            for i in posts:
                if i.author == request.user:
                    self.like_stat += i.like
                    self.dislike_stat += i.dislike
            new_statistic = Statistics(like_stat=self.like_stat, dislike_stat=self.dislike_stat , user=request.user)
            new_statistic.save()

            return "{}{}".format(self.like_stat, self.dislike_stat)
        else:
            print('У данного пользователя нет постов')

    def __str__(self):
        return "{}{}".format(self.like_stat, self.dislike_stat)