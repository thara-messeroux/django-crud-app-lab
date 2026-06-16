from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin dashboard.
    path('admin/', admin.site.urls),

    # Django built-in login/logout routes.
    path('accounts/', include('django.contrib.auth.urls')),

    # TrailTales app pages.
    path('', include('main_app.urls')),
]
