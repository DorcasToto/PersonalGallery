from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.pictures,name = 'pictures'),
    path('location/',views.locations,name = 'location'),
    path('search/', views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)