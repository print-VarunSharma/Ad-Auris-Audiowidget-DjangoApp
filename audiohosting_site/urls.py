"""audiohosting_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from audioApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from audioApp import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from audioApp.views import (
    IndexView,
    audioWidgetTest,
    rebit_2,
    Home
   
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    # Audio Widget Views
    path('audiowidget/', audioWidgetTest.as_view(), name='rebit-widget'),
    path('rebit_2/', rebit_2.as_view(), name='rebit_2'),
    
]
