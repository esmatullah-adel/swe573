"""
URL configuration for PostingItems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('', include('main.urls')),
    path('', include('items.urls')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Include without prefix
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)