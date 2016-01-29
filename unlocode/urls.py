
from django.conf.urls import patterns, url
from unlocode import views

urlpatterns = patterns('',
                       url(r'^$', views.rango, name='rango'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^populate/$', views.populateInitial, name='populate'),
                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^addCategory/$', views.addCategory, name='addCategory'),
                       url(r'^category/(?P<categoryNameSlug>[\w\-]+)/addPage/$', views.addPage, name='addPage'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^userLogin/$', views.userLogin, name='userLogin'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       url(r'^userLogout/', views.userLogout, name='userLogout'),
                       url(r'^loggedin/', views.loggedin, name='loggedin'),
                       )
