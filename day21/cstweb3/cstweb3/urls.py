
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://localhost:8000/core/
    path('core/', include('core.urls')),
    path('', include('core.urls')),
]
