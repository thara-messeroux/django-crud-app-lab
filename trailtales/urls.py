from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django admin dashboard.
    path('admin/', admin.site.urls),

    # Django built-in login/logout routes.
    path('accounts/', include('django.contrib.auth.urls')),

    # TrailTales app pages.
    path('', include('main_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
