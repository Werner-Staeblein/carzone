from django.shortcuts import render
from pages.models import Team
from cars.models import Car
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_data').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_data')
    
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    # nur eindeutige Werte pro Feld holen
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

   
    data = {
        "teams": teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    
    print(model_search, city_search, year_search, body_style_search)
    
    return render(request, 'pages/home.html', data)



def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')