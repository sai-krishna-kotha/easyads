import os
import django
import sys
import random
from faker import Faker

# Step 1: Setup Django environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /easyads/scripts
PROJECT_ROOT = os.path.dirname(BASE_DIR)               # /easyads
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyads.settings')
django.setup()

# Step 2: Import your models
from classifieds.models import Ad, Seller, Category, City

# Step 3: Generate fake data
fake = Faker()
num_ads = 20

sellers = list(Seller.objects.all())
categories = list(Category.objects.all())
cities = list(City.objects.all())

if not sellers or not categories or not cities:
    print("❌ You must have Sellers, Categories, and Cities created first.")
    sys.exit()

for _ in range(num_ads):
    Ad.objects.create(
        seller=random.choice(sellers),
        title=fake.catch_phrase(),
        description=fake.paragraph(nb_sentences=5),
        category=random.choice(categories),
        price=round(random.uniform(1000, 50000), 2),
        city=random.choice(cities),
        status=random.choice(['APPROVED', 'PENDING', 'REJECTED']),
    )

print(f"✅ Successfully created {num_ads} sample ads.")
