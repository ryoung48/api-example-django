from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^doctors/', views.doctors),
    url(r'^appointment/verify/', views.verify_identity),
    url(r'^appointment/finalize/', views.finalize_checkin),
    url(r'^get-token/$', views.get_csrf_token),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
