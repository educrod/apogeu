from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Machine, Customer 
from api.serializers import MachineSerializer, CustomerSerializer
from rest_framework.permissions import IsAuthenticated


class MachineViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

