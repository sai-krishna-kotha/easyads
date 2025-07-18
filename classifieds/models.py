from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    business_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.TextField(blank=True,max_length=200)
    verified = models.BooleanField(default=False)
    wishlist = models.ManyToManyField('Ad', blank=True,related_name="wishlist")
    class Meta:
        db_table = 'seller'
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return f"{self.user.first_name} ({self.business_name})"


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        db_table = 'city'
        ordering = ['name']
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Ad(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'is_staff': True},
        related_name='reviewed_ads'
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ads'
        ordering = ['-created_at']
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return f"{self.title} - ₹{self.price}"

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    wishlist = models.ManyToManyField(Ad, blank=True, related_name='wishlisted_by')
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['user']
        db_table = 'customer'
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_customer_user')
        ]
    def __str__(self):
        return f"{self.user}"