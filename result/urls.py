from asyncore import poll
from django.urls import path
from .views import poll_results, direct_results, total_lga_pu, new_poll_result

urlpatterns = [
    path('poll-results/<int:pk>/', poll_results, name='poll-results'),
    path('direct-results/', direct_results, name='direct-results'),
    path('total-lga/', total_lga_pu, name='total-lga'),
    path('new-result/', new_poll_result, name='new-result'),
]