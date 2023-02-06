from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:taxon_id>',views.taxon_detail,name='taxon_detail'),
    path('taxon_list/',views.taxon_list,name='taxon_list'),
]
