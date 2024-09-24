from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseRedirect  # Import this for redirecting

urlpatterns = [
    path('auth/', include('authentication.urls')),  # Include auth-related URLs
    path('', include('shop.urls')),                # Shop-related URLs
    path('admin/', admin.site.urls),               # Admin panel

    # Redirect 'auth/' to 'auth/login/'
    path('auth/', lambda request: HttpResponseRedirect('/auth/login/')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
