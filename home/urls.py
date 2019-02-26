from django.conf.urls import include,url
from home import views
app_name = 'home'
urlpatterns = [

     #to print a html page ->  url(r'^$', views.ind, name='index'),
     url(r'^$', views.IndexView.as_view(), name='index'),

     # ravi/product/entry
     url(r'^product/entry/$', views.ProductEntry.as_view(), name='product-entry'),

     # ravi/product/2
     url(r'^product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),

     # ravi/product/(?P<pk>[0-9]+)/delete
     url(r'^album/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete'),


]