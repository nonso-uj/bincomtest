from asyncore import poll
from django.urls import path
from .views import states_view, lga_view, ward_view, polls_view

urlpatterns = [
    path('', lga_view, name='lga'),
    path('states/', states_view, name='states'),
    path('ward/<str:pk>/', ward_view, name='ward'),
    path('polls/<str:pk>/', polls_view, name='polls'),
]