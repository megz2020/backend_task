from django.urls import path
from core.views import CoffeeMachineViewSet, CoffeePodViewSet

urlpatterns = [
    path('mcofee/', CoffeeMachineViewSet.as_view({'get': 'list'})),
    path('pods/', CoffeePodViewSet.as_view({'get': 'list'}))
]