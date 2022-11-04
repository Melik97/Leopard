from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_categories',
        null=True,
        blank=True
    )
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse(
            'shop:category_filter',
            args={self.slug}
        )


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        blank=False,
        null=False,
        related_name='products',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='seller/products/%Y/%b/%d/')
    description = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def category_name(self):
        return self.category.name
        
    def get_absolut_url(self):
        return reverse(
            'shop:product_detail',
            args={self.slug, }
        )
