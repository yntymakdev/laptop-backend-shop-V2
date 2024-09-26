from django.urls import path
from .views import *


urlpatterns = [
    path('', LaptopViewSet.as_view({'get': 'list',
                                    'post': 'create'}), name='laptop_list'),
    path('<int:pk>/', LaptopViewSet.as_view({'get': 'retrieve',
                                             'put': 'update', 'delete': 'destroy'}), name='laptop_detail'),

    path('photo/', LaptopPhotoViewSet.as_view({'get': 'list',
                                               'post': 'create'}), name='photo_list'),
    path('photo/<int:pk>/', LaptopPhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='photo_detail'),
]
