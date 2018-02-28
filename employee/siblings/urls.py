from django.conf.urls import url
from .views import (siblings_view ,
					siblings_update_view,
					delete_siblings )


urlpatterns = [
    url(r'create$',siblings_view, name='create') ,
    url(r'update$',siblings_update_view, name='update') ,
    url(r'delete$',delete_siblings, name='delete') ,
    ]
