from django.conf.urls import url 
from bookInventorys import views 
 
urlpatterns = [ 
    url(r'^api/bookInventorys$', views.bookInventory_list),
    url(r'^api/bookInventorys/(?P<pk>[0-9]+)$', views.bookInventory_detail),
    url(r'^api/bookInventorys/published$', views.bookInventory_list_published)
]