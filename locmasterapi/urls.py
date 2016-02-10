from django.conf.urls import url
from locmasterapi import views as locmasterapi_views

urlpatterns = [
    # URL pattern for the UNLocVersionList V1
    url(
        regex=r'^v1/unlocode/$',
        view=locmasterapi_views.V1_LocodeList.as_view(),
        name='v1-list',
    ),
    # URL pattern for the UnLocVersionDetailView V1
    url(
        regex=r'^v1/unlocode/(?P<locode>[\w\-]+)/$',
        view=locmasterapi_views.V1_LocodeDetail.as_view(),
        name='v1-detail',
    ),
    # URL pattern for the UnLocVersionList V0
    url(
        regex=r'^v0/unlocode/',
        view=locmasterapi_views.v0_gone,
        name='v0-list',
    ),
]
