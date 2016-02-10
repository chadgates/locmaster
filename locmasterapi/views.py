from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from unlocode.models import Locode
from locmasterapi.serializers import LocodeSerializer
from django.http import HttpResponseGone

class V1_LocodeList(ListAPIView):
    queryset = Locode.objects.all()
    serializer_class = LocodeSerializer
    lookup_field = 'locode'


class V1_LocodeDetail(RetrieveAPIView):
    queryset = Locode.objects.all()
    serializer_class = LocodeSerializer
    lookup_field = 'locode'


def v0_gone(request):
    apiv0_gone_msg = """APIv0 was removed on January 31, 2016. Please switch to APIv1:
                        <ul>
                            <li>
                                <a href="/api/v1/">APIv1 Endpoint</a>
                            </li>
                            <li>
                                <a href="/apiv1_docs/">APIv1 Documentation</a>
                            </li>
                            <li>
                                <a href="/apiv0_shutdown/">APIv0 shut down notice</a>
                            </li>
                        </ul>
                        """
    return HttpResponseGone(apiv0_gone_msg)
