from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', view.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', view.ProductDetail, name='ProductDetail'),
    url(r'^$', view.ProductList, name='ProductList'),
]