from django.db import models
from users.models import User


class Book(models.Model):
    AVAILABLE = "AV"
    CHECKED_OUT = "CO"
    DAMAGED = "DA"
    LOST = "LO"

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (CHECKED_OUT, 'Checked_out'),
        (DAMAGED, 'Damaged'),
        (LOST, 'Lost'),
    ]

    title = models.CharField(max_length=100)
    author = models.ManyToManyField(
        User, related_name='book_authors')
    owner = models.ForeignKey(
        User, related_name='book_owner', on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(
        User, related_name='book_borrower', on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=AVAILABLE)
    type = models.PositiveSmallIntegerField(choices=(
        (1, "Hardcover"),
        (2, "Paperback"),
        (3, "Digital Copy"),
    ), default=1)
    location = models.PositiveSmallIntegerField(choices=(
        (1, "Exactus Office"),
        (2, "Owner’s Home"),
        (3, "In the Matrix"),
    ), default=1)

    def __str__(self):
        return self.title


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
