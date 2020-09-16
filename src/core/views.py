from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import CoffeeMachine, CoffeePod
from core.serializers import CoffeeMachineSerializer, CoffeePodSerializer


class CoffeeMachineViewSet(ModelViewSet):

    serializer_class = CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'sku_code','water_line_compatible']

    def get_queryset(self):
        return CoffeeMachine.objects.all()


class CoffeePodViewSet(ModelViewSet):

    serializer_class = CoffeePodSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'coffee_flavor', 'pack_size']



    def get_queryset(self):
        return CoffeePod.objects.all()
