from django.conf.urls import url
from locmasterapi import views as locmasterapi_views

urlpatterns = [
    # URL pattern for the UNLocVersionListView
    url(
        regex=r'^v1/unlocode/$',
        view=locmasterapi_views.V1_LocodeList.as_view(),
        name='list',
    ),
    # URL pattern for the UnLocVersionDetailView
    url(
        regex=r'^v1/unlocode/(?P<locode>[\w\-]+)/$',
        view=locmasterapi_views.V1_LocodeDetail.as_view(),
        name='detail',
    ),
]
