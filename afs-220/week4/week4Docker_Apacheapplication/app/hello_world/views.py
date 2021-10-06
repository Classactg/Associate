from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/index.html'
    def get_queryset(self):
        pass
    # return render(request, 'index.html')
class LocationsView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/locations.html'
class GallaryView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/gallary.html'
class AboutView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/about.html'
class ServicesView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/services.html'
class ContactsView(generic.ListView):
    # """Placeholder index view"""
    template_name = '/contacts.html' 

