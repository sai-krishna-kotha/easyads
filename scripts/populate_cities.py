import os
import django
import sys

# Step 1: Add the root directory (where manage.py is) to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /easyads/scripts
PROJECT_ROOT = os.path.dirname(BASE_DIR)               # /easyads
sys.path.append(PROJECT_ROOT)

# Step 2: Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyads.settings')

# Step 3: Setup Django
django.setup()

from user_management.models import City
from django.utils.text import slugify

indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara",
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli",
    "Vasai-Virar", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai",
    "Allahabad", "Ranchi", "Howrah", "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur",
    "Madurai", "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubli–Dharwad", "Mysore"
]

for city_name in indian_cities:
    slug = slugify(city_name)
    obj, created = City.objects.get_or_create(name=city_name, slug=slug)
    if created:
        print(f"Added city: {city_name} ({slug})")
    else:
        print(f"City already exists: {city_name} ({slug})")
