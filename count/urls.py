
#from django.config.urls import url
from django.urls import path
from . import index

urlpatterns = [
    path('',index.count, name='count'),
    path('value/', index.value, name='value'),

]
