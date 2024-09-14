from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from apps.core.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/login/', user_login, name='login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)