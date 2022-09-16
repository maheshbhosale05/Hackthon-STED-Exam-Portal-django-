"""Project URL Configuration

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
from blogs.views import Home,signup,login,application,rules,table,Eligibility,exampattern,syllabus,files,logout,profile,editapplication,alluser,adminlogin,singleuser,edituser,deleteuser,faqs,report


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('application/',application,name="application"),
    path('rules/',rules,name='rules'),
    path('table/',table,name='table'),
    path('Eligibility/',Eligibility,name='Eligibility'),
    path('exampattern/',exampattern,name='exampatter'),
    path('syllabus/',syllabus,name='syllabus'),
    path('files/',files,name='files'),
    path('logout/',logout,name="logout"),
    path('profile/',profile,name="profile"),
    path('editapplication/',editapplication,name='editapplication'),
    path('alluser/',alluser,name='alluser'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('singleuser/<int:id>/',singleuser,name="singleuser"),
    path('edituser/<int:id>/',edituser,name="edituser"),
    path('deleteuser/<int:id>/',deleteuser,name="deleteuser"),
    path('faqs/',faqs,name='faqs'),
    path('report/',report,name='report'),
]
