from django.urls import path, include
from passionatelycurious import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('library/', views.library, name='library'),
    path('mi/', include('machineintelligence.urls')),
]
