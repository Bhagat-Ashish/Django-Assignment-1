from django.contrib import admin
from django.urls import path, include, re_path
from profileApp.views import profile_view
from productsApp.views import product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('home/', include('home.urls')),
    path('contact/', include('contact.urls')),
    re_path(r'^profile/(?P<username>[a-zA-Z0-9_]+)/$', profile_view, name='profile'),
    re_path(r'^products/(?P<category>[a-zA-Z]+)/(?P<product_id>\d+)/$', product_view, name='products'),
]
