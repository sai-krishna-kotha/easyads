import os
import sys
import django
from django.utils.text import slugify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)  
     
sys.path.append(PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyads.settings')

django.setup()

from classifieds.models import Category

categories = [
    "Mobiles", "Electronics & Appliances", "Vehicles", "Furniture", "Real Estate", "Jobs",
    "Services", "Pets", "Books, Sports & Hobbies", "Fashion", "Kids & Babies", "Education",
    "Matrimonial", "Rentals", "Events", "Travel & Tourism", "Freelancers & Gigs",
    "Health & Beauty", "Tools & Machinery", "Business & Industrial", "Agriculture",
    "Art & Collectibles", "Computer & Laptops", "Cameras & Lenses"
]

for name in categories:
    slug = slugify(name)
    category, created = Category.objects.get_or_create(name=name, slug=slug)
    if created:
        print(f"Added Category: {name} ({slug})")
    else:
        print(f"Category already exists: {name} ({slug})")
