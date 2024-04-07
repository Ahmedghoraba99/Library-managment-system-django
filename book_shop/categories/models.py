from django.db import models
from django.urls import reverse


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_category(cls, name, description):
        category = cls(name=name, description=description)
        category.save()
        return category

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, _id):
        try:
            return cls.objects.get(id=_id)
        except:
            return None

    @classmethod
    def search_by_name(cls, name):
        return cls.objects.filter(name__icontains=name)

    @property
    def get_absolute_url(self):
        return reverse('category.show', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Categories'
