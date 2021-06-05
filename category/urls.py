from django.conf.urls import url 
from category import views 
 
urlpatterns = [ 
    url(r'', views.category_list),
    url(r'^(?P<pk>[0-9]+)$', views.category_detail)
]