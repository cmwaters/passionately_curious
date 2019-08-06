from django.urls import path
from passionatelycurious import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('machineintelligence/', views.machineintelligence, name="machineintelligence")
]
