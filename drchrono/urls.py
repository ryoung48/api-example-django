from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

import views

# TODO: maybe modularize appointments? Or rename endpoints

urlpatterns = [
    # main entry point
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # local doctor endpoints
    url(r'^doctors/$', views.doctors),
    # local appointment endpoints
    url(r'^appointment/verify/$', views.verify_patient_identity),
    url(r'^appointment/finalize/$', views.finalize_patient_checkin),
    url(r'^appointment/visit/$', views.visit),
    url(r'^appointment/$', views.get_appointments),
    # utility endpoints
    url(r'^build-kiosk/$', views.build_kiosk),
    url(r'^logout/$', views.logout_user),
    url(r'^auth-check/$', views.logged_in),
    url(r'^get-token/$', views.get_csrf_token),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
