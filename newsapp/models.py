from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username.title()}'

    # def update_rating(auth):
    #     posts = Post.objects.filter(author=auth)
    #     coms = Comment.objects.filter(user=auth.user)
    #     count = 0
    #     for p in posts:
    #         count += p.rating * 3
    #         post_coms = Comment.objects.filter(post=p)
    #         for c in post_coms:
    #             count += c.rating
    #     for c in coms:
    #         count += c.rating
        # auth.rating = count
        # auth.save()


# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)

    # def __str__(self):
    #     return f'{self.name.title()}'


class Post(models.Model):
    news, article = 'N', 'A'
    types = [(news, 'news'), (article, 'article')]
    title = models.CharField(max_length=255, unique=True)
    posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    # type = models.CharField(max_length=1, choices=types, default=news)
    # rating = models.IntegerField(default=0)
    # category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    # def like(self):
    #     self.rating += 1
    #     self.save()
    #
    # def dislike(self):
    #     self.rating -= 1
    #     self.save()
    #
    # def preview(self):
    #     return str(self.text[0:124]) + '...'


# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#
# class Comment(models.Model):
#     posted = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()
#     rating = models.IntegerField(default=0)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def like(self):
    #     self.rating += 1
    #     self.save()
    #
    # def dislike(self):
    #     self.rating -= 1
    #     self.save()
