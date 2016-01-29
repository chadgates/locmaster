from django.conf.urls import url
from unlocode import views

urlpatterns = [
#                       url(r'^$', views.rango, name='rango'),
#                       url(r'^about/$', views.about, name='about'),
                       url(r'^populate/$', views.populateInitial, name='populate'),
                       url(r'^importsubdivisons/$', views.importsubdivisons, name='importsubdivisons'),
                       url(r'^importcountries/$', views.importcountries, name='importcountries'),
#                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/$', views.category, name='category'),
#                       url(r'^addCategory/$', views.addCategory, name='addCategory'),
#                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/addPage/$', views.addPage, name='addPage'),
#                       url(r'^register/$', views.register, name='register'),
#                       url(r'^userLogin/$', views.userLogin, name='userLogin'),
#                       url(r'^restricted/', views.restricted, name='restricted'),
#                       url(r'^userLogout/', views.userLogout, name='userLogout'),
#                       url(r'^loggedin/', views.loggedin, name='loggedin'),
                       ]

