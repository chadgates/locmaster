from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from unlocode.models import Locode
from locmasterapi.serializers import LocodeSerializer


class V1_LocodeList(ListAPIView):
    queryset = Locode.objects.all()
    serializer_class = LocodeSerializer
    lookup_field = 'locode'


class V1_LocodeDetail(RetrieveAPIView):
    queryset = Locode.objects.all()
    serializer_class = LocodeSerializer
    lookup_field = 'locode'

