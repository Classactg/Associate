from django.urls import path

from . import views
print( views.home )
urlpatterns = [
    path('', views.home, name='home'),
    path('orange/', views.orange, name='orange'),
]