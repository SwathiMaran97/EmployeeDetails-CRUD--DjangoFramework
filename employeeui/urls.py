"""employeeui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from emp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),
    path('newemployee/', new_employee_details),
    path('searchemployee/', search_employee_details),
    path('showemployee/', show_employee_details),
    path('editemployee/<int:id>/',edit_employee_details),
    path('deleteemployee/<int:id>/',delete_employee_details),
    path('uploadfile/',upload),
    path('profitanalysis/',chart),
   
]
