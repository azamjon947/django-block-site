from django.urls import path, include
from django.contrib import admin
from website.views import Register



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('website.urls')),
    path('signup/', Register.as_view(), name='signup') 
]
