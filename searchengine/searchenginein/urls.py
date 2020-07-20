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
from django.contrib import admin
from django.urls import path
import usercontrol.views as userview
import search.views as search
import indexing.views as indexing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercontrol/login', userview.LoginView),
    path('usercontrol/newpassword', userview.NewPassword),
    path('usercontrol/passwordrecovery', userview.Password),
    path('search/display', search.Display),
    path('search/searchresults', search.SearchResults),
    path('indexing/inportnew', indexing.Import),
    path('indexing/textmanagement', indexing.Management),
]
