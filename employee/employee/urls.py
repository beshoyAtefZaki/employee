"""employee URL Configuration

"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url ,include
from django.contrib import admin
from mainapp.views import(  home ,
                            EmployeeDetailView,
                            create,
                            update_view,
                            delete_view,
                           
                            )
from search.views import SearchEmployeeListView,search_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home, name='home') ,
    url(r'^create/$',create, name='create') ,
    url(r'^delete/$',delete_view, name='delete') ,
    
    url(r'^update/(?P<slug>[\w-]+)$',update_view,
                     name='update') ,
    url(r'^(?P<slug>[\w-]+)/$',
            EmployeeDetailView.as_view() ,
            name='detail'),

     url(r'^siblings/',
      include('siblings.urls',namespace="siblings")),

     url(r'^salary/', include('salary.urls',
                        namespace="salary")),

     
     url(r'^search',SearchEmployeeListView.as_view() ,
                name='search'),
       url(r'^sarch_api',search_api ,
                name='sarch_api'),
                ]

if settings.DEBUG:
    urlpatterns =  urlpatterns+static(
                settings.STATIC_URL,
			    document_root=settings.STATIC_ROOT)
    urlpatterns =  urlpatterns+static(
                 settings.MEDIA_URL,
				 document_root=settings.MEDIA_ROOT)
