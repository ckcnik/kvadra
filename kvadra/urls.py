"""kvadra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .api_views import GetTextViewSet
from .views import uploadText, getText

get_text = GetTextViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

text_detail = GetTextViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    url(r'^$', uploadText, name='index'),  # главная странца
    url(r'^list/$', getText, name='list-of-text'),  # главная странца
    url(r'^admin/', admin.site.urls),
    url(r'^api/text/$', get_text, name='get-text'),  # main gate
    url(r'^api/text/(?P<pk>[0-9]+)/$', text_detail, name='text-detail'),  # main gate
]
