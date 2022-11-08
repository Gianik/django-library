from django.db import models
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    owner = models.CharField(max_length=30)
    checked_out_by = models.CharField(max_length=30)
    check_out_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30)
    type = models.CharField(max_length=30)


class Comments(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Book, related_name='comments', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse('blog-detail', kwargs={'pk': self.post.id})
