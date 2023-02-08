from django.urls import path
from .views import HomePage, Register, WelcomePage, logoutuser, ConsolePage

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage, name="home-page"),
    path('console/', ConsolePage, name="console-page"),
    path('register/', Register, name="register-page"),
    path('logout/', logoutuser, name='logout'),
    path('welcome/', WelcomePage, name='welcome-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)