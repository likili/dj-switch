"""switch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from blocks.views import index
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [

    path('', index, name="index"),


    path('admin/', admin.site.urls),
]
#
# urlpatterns = [
#     path('', index, name='index'),
#     url(r'^contact/$', ContactView.as_view(), name='contact'),
#     # url(r'^courses/$', ContactView.as_view(), name='courses'),
#     path('courses/', include('courses.urls', namespace='courses')),
#     path('students/', include('student.urls', namespace='students')),
#     path('osago/', include('osago.urls', namespace='osago')),
#     path('admin/', admin.site.urls),
# ]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

urlpatterns += staticfiles_urlpatterns()