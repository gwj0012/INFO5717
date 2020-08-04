"""searchenginein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import indexing.views as indexing
import search.views as search
import usercontrol.views as view
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('', view.LoginView),
    path('search/search', search.Search),
    path('admin/', admin.site.urls),
    path('usercontrol/', include('usercontrol.urls')),
    path('usercontrol/loginaction', view.LoginAction),
    path('search/display', search.Display),
    path('search/searchresults', search.SearchResults),
    path('indexing/inportnew', indexing.Import),
    path('indexing/textmanagement', indexing.Management),
    path(r'captcha/', include('captcha.urls')),
]
