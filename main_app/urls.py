from django.urls import path
from . import views


urlpatterns = [
    # Public homepage.
    path('', views.home, name='home'),

    # Discovery pages.
    path('discoveries/', views.discovery_index, name='discovery-index'),
    path('discoveries/new/', views.discovery_create, name='discovery-create'),
    path('discoveries/<int:discovery_id>/', views.discovery_detail, name='discovery-detail'),
    path('discoveries/<int:discovery_id>/edit/', views.discovery_update, name='discovery-update'),
    path('discoveries/<int:discovery_id>/delete/', views.discovery_delete, name='discovery-delete'),

    # Account creation.
    path('accounts/signup/', views.signup, name='signup'),
]
