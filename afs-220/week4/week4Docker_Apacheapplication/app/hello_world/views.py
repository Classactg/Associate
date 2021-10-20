from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import date
# import calendar
# from calendar import HTMLCalendar

def index(request):
    # year = int(year)
    # month = int(month)
    # if year < 1900 or year > 2099: year = date.today().year
    # month_name = calendar.month_name[month]
    
    # cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'index.html')
# from django.shortcuts import render
# from django.views import generic

# class IndexView(generic.ListView):
#     # """Placeholder index view"""
#     template_name = '/index.html'
#     def get_queryset(self):
#         pass
#     # return render(request, 'index.html')
def MenuView(request):
    return render(request, 'menu.html')
def GallaryView(request):
    return render(request, 'gallary.html')
def AboutView(request):
    return render(request, 'about.html')
def ServicesView(request):
    return render(request, 'services.html')
def ContactsView(request):
    return render(request, 'contacts.html')

