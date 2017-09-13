from django.conf.urls import url
from .views import index
from .views import add_activity

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'add_activity/$', add_activity, name='add_activity'),
]
