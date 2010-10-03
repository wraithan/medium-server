from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate
from registration.views import register
from profiles.models import Contributor

urlpatterns = patterns('',
                       url(r'^', include('medium.main.urls')),
                       url(r'^accounts/', include('registration.urls')),
)

urlpatterns += patterns('',
                        url(r'^activate/(?P<activation_key>\w+)/$',
                            activate,
                            name='registration_activate'),
                        url(r'^login/$',
                            auth_views.login,
                            {'template_name': 'registration/login.html'},
                            name='auth_login'),
                        url(r'^logout/$',
                            auth_views.logout,
                            {'template_name': 'registration/logout.html'},
                            name='auth_logout'),
                        url(r'^password/change/$',
                            auth_views.password_change,
                            name='auth_password_change'),
                        url(r'^password/change/done/$',
                            auth_views.password_change_done,
                            name='auth_password_change_done'),
                        url(r'^password/reset/$',
                            auth_views.password_reset,
                            name='auth_password_reset'),
                        url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                            auth_views.password_reset_confirm,
                            name='auth_password_reset_confirm'),
                        url(r'^password/reset/complete/$',
                            auth_views.password_reset_complete,
                            name='auth_password_reset_complete'),
                        url(r'^password/reset/done/$',
                            auth_views.password_reset_done,
                            name='auth_password_reset_done'),
                        url(r'^register/$',
                            register,
                            kwargs={'profile_callback': Contributor.objects.create},
                            name='registration_register'),
                        url(r'^register/complete/$',
                            direct_to_template,
                            {'template': 'registration/registration_complete.html'},
                            name='registration_complete'),
                        )
