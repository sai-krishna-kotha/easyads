<<<<<<< HEAD
from classifieds.models import Category, City
=======
from user_management.models import Category, City
>>>>>>> 260fb9cf69e02f6c538eae5c14c1c6b8f96d97d5

def global_search_context(request):
    return {
        'categories': Category.objects.all(),
        'cities': City.objects.all(),
    }
