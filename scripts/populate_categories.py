# scripts/populate_categories.py

import os
import sys
import django
from django.utils.text import slugify

# Step 1: Add the root directory (where manage.py is) to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /easyads/scripts
PROJECT_ROOT = os.path.dirname(BASE_DIR)               # /easyads
sys.path.append(PROJECT_ROOT)

# Step 2: Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyads.settings')

# Step 3: Setup Django
django.setup()

# Step 4: Import your Category model
from app2_ads.models import Category

# Step 5: Define categories
categories = [
    "Mobiles", "Electronics & Appliances", "Vehicles", "Furniture", "Real Estate", "Jobs",
    "Services", "Pets", "Books, Sports & Hobbies", "Fashion", "Kids & Babies", "Education",
    "Matrimonial", "Rentals", "Events", "Travel & Tourism", "Freelancers & Gigs",
    "Health & Beauty", "Tools & Machinery", "Business & Industrial", "Agriculture",
    "Art & Collectibles", "Computer & Laptops", "Cameras & Lenses"
]

# Step 6: Populate DB
for name in categories:
    slug = slugify(name)
    category, created = Category.objects.get_or_create(name=name, slug=slug)
    if created:
        print(f"✅ Created: {name} ({slug})")
    else:
        print(f"⚠️ Already exists: {name} ({slug})")
