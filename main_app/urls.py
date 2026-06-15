from django.urls import path
from . import views


urlpatterns = [
    # Shows the TrailTales homepage.
    path('', views.home, name='home'),

    # Shows all saved trail discoveries.
    path('discoveries/', views.discovery_index, name='discovery-index'),
]