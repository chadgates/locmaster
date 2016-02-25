from django.conf.urls import url
from mylocation import views as mylocation_views
from django.views.generic import TemplateView

urlpatterns = [
    # URL pattern for the UNLocVersionListView
    url(
        regex=r'^welcome/$',
        view=TemplateView.as_view(template_name='mylocation/welcome.html'),
        name='welcome',
    ),
    # URL pattern for the FunctionDetailView
    # URL pattern for the FunctionCreateView
    url(
        regex=r'^function/create/$',
        view=mylocation_views.FunctionCreate.as_view(),
        name='function-create',
    ),
    url(
        regex=r'^function/(?P<pk>[\w\-]+)/$',
        view=mylocation_views.FunctionDetail.as_view(),
        name='function-detail',
    ),
    # URL pattern for the FunctionUpdateView
    url(
        regex=r'^function/(?P<pk>[\w\-]+)/update/$',
        view=mylocation_views.FunctionUpdate.as_view(),
        name='function-update',
    ),
    # URL pattern for the FunctionUpdateView
    url(
        regex=r'^function/(?P<pk>[\w\-]+)/delete/$',
        view=mylocation_views.FunctionDelete.as_view(),
        name='function-delete',
    ),
    # URL pattern for the FunctionListview
    url(
        regex=r'^function/$',
        view=mylocation_views.FunctionList.as_view(),
        name='function-list',
    ),
]
