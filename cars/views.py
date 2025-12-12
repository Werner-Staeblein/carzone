from django.shortcuts import render, get_object_or_404
from cars.models import Car

def cars(request):
    return render(request, 'cars/cars.html')


def search(request):
    cars = Car.objects.order_by('-created_data')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
        
    data = {
        'cars': cars,
    }
    
    return render(request, 'cars/search.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
	
    data = {'single_car': single_car}
    
    return render (request, 'cars/car_detail.html', data)



