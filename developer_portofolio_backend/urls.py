from django4_recaptcha_admin_login import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import root_route, logout_route


urlpatterns = [
    path('', root_route),
    # Admin Url's
    path('admin/', admin.site.urls),
    # All-Auth Url's
    # our logout route has to be above the default one to be matched first
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    # Profiles Url's
    path('', include('profiles.urls')),
    # Projects Url's
    path('', include('projects.urls')),
    # Contact Url's
    path('', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
