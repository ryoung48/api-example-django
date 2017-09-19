from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

import views

# TODO: maybe modularize appointments? Or rename endpoints


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^doctors/api/', views.doctors_api),
    url(r'^doctors/$', views.doctors),
    url(r'^doctor/status/', views.doctor_status_update),
    url(r'^patients/api/', views.patients_api),
    url(r'^appointments/api', views.appointments_api),
    url(r'^appointment/verify/', views.verify_identity),
    url(r'^appointment/finalize/', views.finalize_checkin),
    url(r'^appointment/visit/', views.visit),
    url(r'^appointment/(?P<doctor_id>[0-9]+)/', views.get_appointments),
    url(r'^get-token/$', views.get_csrf_token),
    url(r'^home/$', views.home),
    url(r'^secure/$', views.secure),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
