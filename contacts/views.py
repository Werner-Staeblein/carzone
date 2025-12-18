from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def inquiry(request):
    if request.method == "POST":
        # Werte aus dem Formular (name="...") abholen
        car_id = request.POST.get('car_id')
        car_title = request.POST.get('car_title')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Neues Contact-Objekt erstellen und speichern
        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message,
        )
        contact.save()

        # Erfolgsmeldung für den User
        messages.success(request, 'Your request has been submitted. We will contact you soon')

        # Weiterleitung zurück zur Detailseite des Autos
        return redirect('/cars/' + str(car_id))
