from django.db import models
# ignore err
from django.urls import reverse
from categories.models import Category


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/books', null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, related_name="allCategories")
    # dear instructor, I know null=true is not right, but it's but for the old db

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books.show', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('books.delete', args=[str(self.id)])

    def get_update_url(self):
        return reverse('books.update', args=[str(self.id)])

    @property
    def imageURL(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url
