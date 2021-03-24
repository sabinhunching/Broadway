from django.shortcuts import render

# Create your views here.
from contacts.models import Contacts


def show_contact(request):
    contact = Contacts.objects.all()
    return render(request, 'contact.html', {'contact': contact})