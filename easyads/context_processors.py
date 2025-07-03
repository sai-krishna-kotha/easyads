from classifieds.models import Category, City
def global_search_context(request):
    return {
        'categories': Category.objects.all(),
        'cities': City.objects.all(),
    }
