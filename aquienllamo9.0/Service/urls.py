from django.conf.urls import url
from . import views
from Comment.views import Com 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ url(r'^$', views.Categories, name='Categories'),
				url(r'^All/$',views.All, name='New'),
				url(r'^New/$',views.New, name='All'),
				url(r'^(?P<Name>[a-zA-Z]+)/$',views.Cat, name='Category'),
				url(r'^(?P<Name>.*)/(?P<NameService>.*)/Comment/',Com, name='Comment'),
				url(r'^(?P<Name>.*)/(?P<NameService>.*)/$',views.Serv, name='Serv'),
				]