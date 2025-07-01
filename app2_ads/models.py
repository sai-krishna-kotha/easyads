from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from app1_users.models import User  # Assuming Seller is linked via User

# ------------------ Seller Model ------------------
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    business_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.TextField(blank=True,max_length=200)
    verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'seller'
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return f"{self.user.first_name} ({self.business_name})"

    



# ------------------ Category Model ------------------
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


# ------------------ City Model ------------------
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


# ------------------ Ad Model ------------------
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
    # image = models.ImageField(upload_to='ads/', blank=True, null=True)
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
    wishlist = models.ManyToManyField(Ad, related_name='wishlisted_by')