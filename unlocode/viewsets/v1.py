from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from unlocode.models import Locode
from unlocode.serializers import LocodeSerializer


class LocodeList(ListAPIView):
    queryset = Locode.objects.all()
    serializer_class = LocodeSerializer
    lookup_field = 'locode'


class LocodeDetail(RetrieveAPIView):
    queryset = Locode.objects.all().order_by('locode', 'version').distinct('locode')
    serializer_class = LocodeSerializer
    lookup_field = 'locode'
