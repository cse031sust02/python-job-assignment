from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('progress_demo/', include('progress_demo.urls')),
]
