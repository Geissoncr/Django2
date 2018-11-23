from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('coral/', include('coral.urls')),
    path('admin/', admin.site.urls),
]
