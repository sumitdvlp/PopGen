from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

app_name='JobSchd'
## loof for cross site request forgery
urlpatterns = [

    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(),name='user_details'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', auth_views.login,{'template_name': 'JobSchd/login.html'},name='auth_login'),

    url(r'^logout/$', auth_views.logout,{'template_name': 'registration/logout.html'},name='auth_logout'),

    url(r'^jobform_final/create/$', views.JobFinalCreate.as_view(), name='jobform_final'),
    url(r'^jobform_final/(?P<pk>\d+)/update/$', views.JobFinalUpdate.as_view(), name='jobform_final_update'),
    url(r'^jobform_final/(?P<pk>\d+)/delete/$', views.JobFinalDelete.as_view(), name='jobform_final_delete'),

    url(r'^team/', views.team, name='team'),

    url(r'^joblist/$', views.JobFinalList.as_view()),
    url(r'^joblist/(?P<pk>[0-9]+)/$', views.JobFinalDetail.as_view()),


    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),



]
