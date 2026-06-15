from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Opens Django's built-in admin dashboard.
    path('admin/', admin.site.urls),

    # Sends normal website pages to main_app.
    path('', include('main_app.urls')),
]