from django.conf.urls import url 
from product import views 
 
urlpatterns = [ 
    url(r'', views.product_list),
    url(r'^(?P<pk>[0-9]+)$', views.product_detail)
]