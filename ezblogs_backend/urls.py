from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls')), 
    path('api/visualizer/', include('visualizer.urls')),
   
]
