from django.conf.urls import url
from unlocode import views as unlocode_views
from unlocode.viewsets import v0 as v0_views
from unlocode.viewsets import v1 as v1_views


urlpatterns = [
    # URL pattern for the UNLocVersionListView
    url(
        regex=r'^versions/$',
        view=unlocode_views.UnLocVersionList.as_view(),
        name='list',
    ),
    # URL pattern for the UnLocVersionDetailView
    url(
        regex=r'^versions/(?P<pk>[\w\-]+)/$',
        view=unlocode_views.UnLocVersionDetail.as_view(),
        name='detail',
    ),

    url(
        regex=r'^version/create/$',
        view=unlocode_views.UnLocVersionCreate.as_view(),
        name='create'
    ),

    # URL pattern for the UnLocVersionUpdateView
    url(
        regex=r'^version/(?P<pk>[\w\-]+)/$',
        view=unlocode_views.UnLocVersionUpdate.as_view(),
        name='update',
    ),

    # URL pattern for the UnLocVersionDeleteView
    url(
        regex=r'^version/(?P<pk>[\w\-]+)/delete/$',
        view=unlocode_views.UnLocVersionDelete.as_view(),
        name='delete',
    ),
    #                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/$', views.category, name='category'),
    #                       url(r'^addCategory/$', views.addCategory, name='addCategory'),
    #                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/addPage/$', views.addPage, name='addPage'),
    #                       url(r'^register/$', views.register, name='register'),
    #                       url(r'^userLogin/$', views.userLogin, name='userLogin'),
    #                       url(r'^restricted/', views.restricted, name='restricted'),
    #                       url(r'^userLogout/', views.userLogout, name='userLogout'),
    #                       url(r'^loggedin/', views.loggedin, name='loggedin'),

    url(
        regex=r'^populate/$',
        view=unlocode_views.Populate.as_view(),
        name='populate',
    ),
    url(
        regex=r'^locodeinfo/$',
        view=unlocode_views.LocodeInfo.as_view(),
        name='populate',
    ),
    url(
        regex=r'^code/(?P<locode>[\w\-]+)/$',
        view=unlocode_views.UnLocodeList.as_view(),
        name='list-code',
    ),
    url(
        regex=r'^code/$',
        view=unlocode_views.UnLocodeSearch.as_view(),
        name='list-search',
    ),

    # URL pattern for the UNLocVersionList V1
    url(
        regex=r'^api/v1/$',
        view=v1_views.LocodeList.as_view(),
        name='v1-list',
    ),
    # URL pattern for the UnLocVersionDetailView V1
    url(
        regex=r'^api/v1/(?P<locode>[\w\-]+)/$',
        view=v1_views.LocodeDetail.as_view(),
        name='v1-detail',
    ),
    # URL pattern for the UnLocVersionList V0
    url(
        regex=r'^api/v0/',
        view=v0_views.gone,
        name='v0-list',
    ),
]
