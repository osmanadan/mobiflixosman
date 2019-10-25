"""mobflix path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
"""

from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='My API title')),
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    # path('', include('staff.urls')),
]
